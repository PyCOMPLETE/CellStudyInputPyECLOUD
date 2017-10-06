from __future__ import division
import numpy as np
from scipy.constants import c, e, m_p

import n_photons

# Pull these names to the namespace for backward compatibility
from materials import materials, materials2, \
    materials_baglin, materials_baglin2, \
    conservative, optimistic
from magnet_strengths import magnets

def arr(x):
    return np.array(x, dtype=float)

def b_rho_proton(energy_eV, m=m_p, q=e):
    energy_tot = energy_eV*e + m*c**2
    p = np.sqrt((energy_tot/c)**2 - m**2*c**2)
    return p/q

# Only ultrarelativistic if B/B_skew are given
def get_b_multip(energy_eV, B_eV=None, B_skew_eV=None, k=None, k_skew=None, **kwargs):
    b_multip = None
    b_skew = None
    b_rho = b_rho_proton(energy_eV)
    if B_eV is not None:
        b_multip = arr(B_eV) * energy_eV
    if B_skew_eV is not None:
        b_skew = arr(B_skew_eV) * energy_eV
    if k is not None:
        b_multip = arr(k) * b_rho
    if k_skew is not None:
        b_skew = arr(k_skew) * b_rho

    if b_multip is None:
        b_multip = np.zeros_like(b_skew, float)
    if b_skew is None:
        b_skew = np.zeros_like(b_multip, float)

    return list(b_multip), list(b_skew)


def get_complete_photoemission_info(energy_eV, R_i, Y_i, Y_r, **kwargs):
    n_photons_meter = n_photons.n_photons_meter(energy_eV)
    ri = R_i
    yi = Y_i
    yr = Y_r
    ni = (1-ri)*yi
    nr = ri*yr
    nt = ni+nr
    r = nr/nt
    k_pe_st = n_photons_meter*nt

    dict_out = {
        'Ri': ri,
        'Yi_star': yi,
        'Yr_star': yr,
        'n_gmamma':n_photons_meter,
        'Ni': ni,
        'Nr': nr,
        'Nt': nt,
        'refl_frac':r,
        'k_pe_st': k_pe_st}

    return dict_out


def get_k_pe_st_and_r(energy_eV, R_i, Y_i, Y_r, **kwargs):

    dict_out = get_complete_photoemission_info(energy_eV, R_i, Y_i, Y_r, **kwargs)
    return dict_out['k_pe_st'], dict_out['refl_frac']

