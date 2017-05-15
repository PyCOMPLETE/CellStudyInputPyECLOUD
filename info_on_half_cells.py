from __future__ import division, print_function
import os
import re

from twiss_file_utils import TfsLine, HalfCell


# Config
vkicker_is_hkicker = False
no_ds_in_mag_len_dict = True
twiss_file_name_tfs = os.path.dirname(os.path.abspath(__file__)) + '/twiss_lhcb1_2.tfs'

re_arc_start = re.compile('(S)\.ARC\.(\d\d)\.B1')
re_arc_end = re.compile('E\.ARC\.\d\d\.B1')
re_sbend_hc = re.compile('^"MB\.[ABC](\d+[LR]\d+)\.B1"$')

re_ds_start = re.compile('(S)\.DS\.([RL]\d)\.B1')
re_ds_end = re.compile('E\.DS\.([RL]\d)\.B1')

# State Machine
look_for_arc = 0
in_arc = 1
in_prefix = 2
in_ds = 3
look_for_ds = 4
status = in_prefix

hc_name = ''
arc = None
half_cell = None
arc_hc_dict = {}
tfs_file = open(twiss_file_name_tfs, 'r')


for line_n, line in enumerate(iter(tfs_file)):
    split = line.split()
    if status == in_prefix:
        if '$' in line:
            status = look_for_arc
    elif status == look_for_arc:
        if re_arc_start.search(line):
            status = in_arc
            arc = ''.join(re_arc_start.search(line).groups())
            arc_half_cells = []
            this_hc = HalfCell(None)
            arc_hc_dict[arc] = arc_half_cells
    elif status == in_arc:
        if re_arc_end.search(line) is not None:
            status = look_for_arc
        else:
            this_name = split[0]
            info = re_sbend_hc.search(this_name)
            if info is not None:
                hc_name = info.group(1)
                if hc_name != this_hc.name:
                    if 1 < this_hc.length < 53:
                        print('length smaller than 53', line_n, this_name)
                    this_hc = HalfCell(hc_name)
                    arc_half_cells.append(this_hc)
            this_line = TfsLine(line, vkicker_is_hkicker)
            this_hc.add_line(this_line)

            if this_hc.length > 54:
                print('length larger than 54:', line_n, this_name)


tfs_file.close()

# Find out how often each half cell type appears in the LHC
type_occurence_dict = {}
for arc, arc_half_cells in arc_hc_dict.iteritems():
    for cell_ctr, hc in enumerate(arc_half_cells):
        hc.create_dict()
        hc.round_dict(precision=2)
        for key, subdict in type_occurence_dict.iteritems():
            if hc.len_type_dict == subdict['dict']:
                subdict['n'] += 1
                subdict['cells'].append((arc, hc.name, cell_ctr))
                break
        else:
            type_occurence_dict[hc.name] = {
                    'dict': hc.len_type_dict,
                    'n': 1, 'cell': hc,
                    'cells': [(arc, hc.name, cell_ctr)]}

mag_len_dict = {}
for arc, arc_half_cells in arc_hc_dict.iteritems():
    for hc in arc_half_cells:
        if not no_ds_in_mag_len_dict or no_ds_in_mag_len_dict and hc.length > 53:
            for key, length in hc.len_type_dict.iteritems():
                if type(length) is not list:
                    if key not in mag_len_dict:
                        mag_len_dict[key] = {}
                    if length not in mag_len_dict[key]:
                        mag_len_dict[key][length] = 0
                    mag_len_dict[key][length] += 1

