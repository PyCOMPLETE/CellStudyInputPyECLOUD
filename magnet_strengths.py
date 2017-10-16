from __future__ import division
import numpy as np
def arr(x):
    return np.array(x, dtype=float)

# Specify either B and/or B_skew per eV of beam energy
#   or k and/or k_skew
magnets = {}
magnets['MB'] = {
    'B_eV': arr([8.33/7000e9]),
}
magnets['MQ'] = {
    'B_eV': arr([0., 12.1/450e9]),
}
magnets['Drift'] = {
    'B_eV': arr([0.]),
}
magnets['MCBH'] = {
    'B_eV': arr([2.93/7000e9]),
}
magnets['MCBV'] = {
    'B_skew_eV': arr([2.5/7000e9]),
}
magnets['MS'] = {
    'k': arr([0, 0, 0.07]),
}
magnets['MS2'] = {
    'k': arr([0, 0, -0.12]),
}
magnets['MO'] = {
    'B_eV': arr([0, 0, 0, 6.31e4/7e12]), # design report: max field
    # old value of k = 16 was probably incorrect
}

