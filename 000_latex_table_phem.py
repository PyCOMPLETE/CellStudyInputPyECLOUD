from __future__ import division
import create_pyecloud_input as cgi

header = '\t'+r"""Type &
$R_i$ &
$R_e$ &
$Y_i$ &
$Y_r$ &
$Y_i^*$ &
$Y_r^*$ &
$N_i$ &
$N_r$ &
$N_t$ &
$R$ &
k\_pe\_st
\\ \hline
"""
header = header.replace('\n',' ')

lines = []
for type_, material in cgi.materials.iteritems():
    ri = material['R_i']
    rr = material['R_r']
    yi = material['Y_i']
    yr = material['Y_r']
    yi2 = yi * (1-ri)
    yr2 = yr * (1-rr)
    ni = (1-ri)*yi
    nr = ri*yr
    nt = ni+nr
    r, k_pe_st = cgi.get_k_pe_st_and_r(6.5e12, type_)


    line = '\t%s &' % type_
    line += '%.1f &' % (ri*100)
    line += '%.1f &' % (rr*100)
    line += '%.1e &' % yi2
    line += '%.1e &' % yr2
    line += '%.1e &' % yi
    line += '%.1e &' % yr
    line += '%.1e &' % ni
    line += '%.1e &' % nr
    line += '%.1e &' % nt
    line += '%.1e &' % r
    line += '%.1e' % k_pe_st
    line += r'\\'

    lines.append(line)

print(header)
print('\n'.join(lines))

