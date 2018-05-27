import n_photons as nph
import numpy as np
import matplotlib.pyplot as plt
import LHCMeasurementTools.mystyle as ms

# bending radius standard LHC MB
rho_MB = nph.lhc_bending_radius

# bending radius 11T dipole
rho_11T = 2.12e3

ene_obs_eV = 7e12

ene_ele_spect_eV = np.logspace(0, 3, 1000)

rho_vect = [rho_MB, rho_11T]
L_vect = [14.3, 2*5.3]
name_cases = ['1 x MB', '2 x MBH']

E_vect_eV = np.linspace(0.45e12, 8e12, 1000)

plt.close('all')
ms.mystyle_arial(fontsz=16, dist_tick_lab=5)

fig_awf = plt.figure(1)
spawgf = fig_awf.add_subplot(1,1,1)

fig_tot = plt.figure(2)
sptot = fig_tot.add_subplot(1,1,1)

fig_xmag = plt.figure(3)
spxmag = fig_xmag.add_subplot(1,1,1)

fig_spect = plt.figure(4)
spspect = fig_spect.add_subplot(1,1,1)

for rho, name, length in zip(rho_vect, name_cases, L_vect):
	#number of photons above Work Function of copper
	n_photons_aWF = nph.n_photons_meter(E_vect_eV, rho, nph.copper_work_function_eV)
	spawgf.plot(E_vect_eV/1e12, n_photons_aWF, label=name, lw=2.)

	#number of photons above Work Function of copper
	n_photons_tot= nph.n_photons_meter(E_vect_eV, rho, 0.)
	sptot.plot(E_vect_eV/1e12, n_photons_tot, label=name, lw=2.)

	#number of photons above Work Function of copper per magnet
	spxmag.plot(E_vect_eV/1e12, n_photons_aWF*length, label=name, lw=2.)

	# plot spectra
	dn_dE = nph.spectral_at_energy(ene_ele_spect_eV, ene_obs_eV, rho)
	spspect.loglog(ene_ele_spect_eV, dn_dE, label=name, lw=2.)

spspect.axvline(nph.copper_work_function_eV, color='k', lw=2)

for sp in [spawgf, sptot, spxmag]:
	sp.grid('on')
	sp.set_xlabel('Energy [TeV]')
	sp.legend(loc='upper left', prop={'size':16})
	sp.ticklabel_format(style='sci', scilimits=(0,0),axis='y')

for sp in [spawgf, sptot]:	
	sp.set_ylabel('N. emitted photons per proton per meter')

spxmag.set_ylabel('N. emitted photons per proton per turn')	

spspect.set_ylim(bottom=1e-20)
spspect.set_xlabel('Photon energy [eV]')
spspect.legend(loc='upper right', prop={'size':16})
spspect.grid('on')
spspect.set_ylabel('dN/dE')

for fig in [fig_awf, fig_tot, fig_xmag, fig_spect]:
	fig.set_facecolor('w')
	fig.subplots_adjust(bottom=.12)

for fig in [fig_xmag, fig_awf]:
	fig.suptitle('Photons with energy larger than Cu work function')


fig_tot.savefig('photons_tot.png', dpi=200)
fig_awf.savefig('photons_above_wf.png', dpi=200)
fig_xmag.savefig('photons_per_mag.png', dpi=200)
fig_spect.savefig('photon_spectrum.png', dpi=200)




plt.show()


