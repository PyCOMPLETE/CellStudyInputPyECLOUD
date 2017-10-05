from __future__ import division

# Baglin 1998
#Photoelectron yield and photon reflectivity from
#candidate LHC vacuum chamber materials with
#implications to the vacuum chamber design
#
# No photon scrubbing taken into account

materials_baglin = {}
materials_baglin['Cu co-lam. with sawtooth'] = {
    'R_i': 1.8e-2,
    'Y_i': 0.053,
    'R_r': 80.9e-2,
    'Y_r': 0.114,
}

materials_baglin['Cu co-lam.'] = {
    'R_i': 80e-2,
    'Y_i': 0.114,
    'R_r': 80e-2,
    'Y_r': 0.114,
}

# Baglin 2001
# Measurements at EPA of vacuum and electron-cloud related effects

# After photon scrubbing, the yields are reduced by a factor of 4.7

materials_baglin2 = {}
materials_baglin2['Cu co-lam. with sawtooth'] = {
    'R_i': 8e-2,
    'Y_i': 0.011,
    'R_r': 80.9e-2,
    'Y_r': 0.114/4.7,
}
materials_baglin2['Cu co-lam.'] = {
    'R_i': 80.9e-2,
    'Y_i': 0.114/4.7,
    'R_r': 80.9e-2,
    'Y_r': 0.114/4.7,
}


# In the photoelectron note, the reflectivities published in
# Mahne 2004 are taken into account.
# Photon reflectivity distributions from the LHC beam screen
# and their implications on the arc beam vacuum system

# Reflectivity of sawtooth -> 10e-2
# Reflectivity elsewhere   -> 82e-2

refl_sawtooth_corrected = 10e-2
refl_smooth_corrected = 82e-2

corrected_reflectivities = {
    'Cu co-lam. with sawtooth': {
        'R_i': refl_sawtooth_corrected,
        'R_r': refl_smooth_corrected,
    },
    'Cu co-lam.': {
        'R_i': refl_smooth_corrected,
        'R_r': refl_smooth_corrected,
    },
}

# For conservative and optimistic estimate, adjust the yields from
# the two Baglin papers by those from the Mahne papers.
conservative = materials ={}
optimistic = materials2 = {}

for baglin_material, corrected_material in [
    (materials_baglin, conservative),
    (materials_baglin2, optimistic),
]:
    for material_type in ('Cu co-lam. with sawtooth', 'Cu co-lam.'):
        corrected_material[material_type] = {}
        r_i = corrected_material[material_type]['R_i'] = corrected_reflectivities[material_type]['R_i']
        r_r = corrected_material[material_type]['R_r'] = corrected_reflectivities[material_type]['R_r']
        corrected_material[material_type]['Y_i'] = baglin_material[material_type]['Y_i']*(1-baglin_material[material_type]['R_i'])/(1-r_i)
        corrected_material[material_type]['Y_r'] = baglin_material[material_type]['Y_r']*(1-baglin_material[material_type]['R_r'])/(1-r_r)

