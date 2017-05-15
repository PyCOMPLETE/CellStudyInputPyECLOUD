from __future__ import division
import numpy as np
from scipy.constants import c

import n_photons

materials = {}
materials['Cu co-lam. with sawtooth'] = {
    'R_i' : 10e-2,
    'Y_i' : 0.053,
    'R_r' : 82e-2,
    'Y_r' : 0.114,
}

materials['Cu co-lam.'] = {
    'R_i' : 82e-2,
    'Y_i' : 0.114,
    'R_r' : 82e-2,
    'Y_r' : 0.114,
}

arr = lambda x: np.array(x, dtype=float)
magnets = {}

magnets['MB'] = {
    'B': arr([8.33/7000e9]),
}
magnets['MQ'] = {
    'B': arr([0., 12.1/450e9]),
}
magnets['Drift'] = {
    'B': arr([0.]),
}
magnets['MCBH'] = {
    'B': arr([2.93/7000e9]),
}
magnets['MCBV'] = {
    'B_skew': arr([2.5/7000e9]),
}
magnets['MS'] = {
    'k': arr([0, 0, 0.07]),
}
magnets['MS2'] = {
    'k': arr([0, 0, -0.12]),
}
magnets['MO'] = {
    'k': arr([0, 0, 0, 16]),
}

keys = magnets.keys()

# Only ultrarelativistic
def get_b_multip(key, energy_eV):
    magnet = magnets[key]
    b_skew = None
    if 'B' in magnet and 'B_skew' in magnet:
        b_multip = magnet['B'].copy()
        b_skew = magnet['B_skew'].copy()
    elif 'B' in magnet:
        b_multip = magnet['B'].copy()
    elif 'B_skew' in magnet:
        b_skew = magnet['B_skew'].copy()
        b_multip = np.zeros_like(b_skew)
    elif 'k' in magnet and 'k_skew' in magnet:
        b_multip = np.zeros_like(magnet['k'])
        b_skew = np.zeros_like(magnet['k_skew'])

        for in_arr, out_arr in zip([magnet['k'], magnet['k_skew']], [b_multip, b_skew]):
            for order, k in enumerate(in_arr):
                out_arr[order] = k/c
    elif 'k' in magnet:
        b_multip = np.zeros_like(magnet['k'])
        for order, k in enumerate(magnet['k']):
            b_multip[order] = k/c
    elif 'k_skew' in magnet:
        b_multip = np.zeros_like(magnet['k_skew'])
        b_skew = np.zeros_like(magnet['k_skew'])
        for order, k in enumerate(magnet['k_skew']):
            b_skew[order] = k/c

    b_multip *= energy_eV
    if b_skew is not None:
        b_skew *= energy_eV

    return b_multip, b_skew

def get_k_pe_st_and_r(energy_eV, key):
    material = materials[key]
    n_photons_meter = n_photons.n_photons_meter(energy_eV)
    #material = materials[material_name]
    ri = material['R_i']
    yi = material['Y_i']
    yr = material['Y_r']
    ni = (1-ri)*yi
    nr = ri*yr
    nt = ni+nr
    r = nr/nt
    k_pe_st = n_photons_meter*nt

    return k_pe_st, r

