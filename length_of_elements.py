from __future__ import division
import numpy as np

import info_on_half_cells as info
import create_pyecloud_input as cpi


mag_len_dict = info.mag_len_dict
n_cells = sum(mag_len_dict['Total'].values())

madx_key_dict ={
    'DRIFT' :       'Drift',
    'HKICKER':      'MCBH',
    'VKICKER':      'MCBV',
#    'MULTIPOLE':    'MQ',
    'OCTUPOLE':     'MO',
    'QUADRUPOLE':   'MQ',
    'SBEND':        'MB',
    'SEXTUPOLE':    'MS',
}


mag_len_dict_avg = {}
for key, len_occurence_dict in mag_len_dict.iteritems():
    if key in madx_key_dict:
        lengths = np.array(len_occurence_dict.keys())
        occurences = np.array(len_occurence_dict.values())
        new_key = madx_key_dict[key]
        if new_key in mag_len_dict_avg:
            old_val = mag_len_dict_avg[new_key]
            print new_key
        else:
            old_val = 0
        mag_len_dict_avg[new_key] = np.sum(lengths*occurences)/n_cells + old_val
    elif 'Total' in key:
        pass
    else:
        print('Neglected: %s' % key)

# Alternating focussing and defocussing sextupoles
mag_len_dict_avg['MS2'] = mag_len_dict_avg['MS']/2
mag_len_dict_avg['MS'] = mag_len_dict_avg['MS']/2

if __name__ == '__main__':
    # Prints out a latex table of magnets
    magnets = cpi.magnets

    devices = (
        'Drift',
        'MB',
        'MCBH',
        'MCBV',
        'MQ',
        'MS',
        'MS2',
        'MO',
    )

    for key in devices:
        subdict = mag_len_dict_avg[key]
        B_multip, B_skew = cpi.get_b_multip(magnets[key], 6.5e12)
        length = mag_len_dict_avg[key]
        if B_skew is None:
            B_skew = '-'
        else:
            B_skew = repr([ float('%.2f' % x) for x in B_skew])
        B_multip = repr([ float('%.2f' % x) for x in B_multip])
        print r'%s & %.2f & %s & %s \\' % (key, length, B_multip, B_skew)
