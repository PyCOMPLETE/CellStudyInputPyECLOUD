from __future__ import division
import os
import argparse
import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import m_e, e

import LHCMeasurementTools.mystyle as ms

parser = argparse.ArgumentParser()
parser.add_argument('-o')
parser.add_argument('--noshow', action='store_true')
args = parser.parse_args()

plt.close('all')
ms.mystyle(12)

delta_x = 2*18e-3
energy_eV = np.linspace(0.1, 40, 1000)

fig = ms.figure('Time needed')
sp = plt.subplot(2,2,1)
sp.grid(True)
sp.set_xlabel('Energy [eV]')
sp.set_ylabel('Time [ns]')

angles = np.arange(0,81,10)
for ctr, angle in enumerate(angles):
    color = ms.colorprog(ctr, angles)
    angle_rad = angle/180*np.pi
    velocity = np.sqrt(2*energy_eV*e/m_e)
    delta_t = delta_x/np.cos(angle_rad)/velocity
    label = '%i' % angle
    sp.semilogy(energy_eV, delta_t*1e9, label=label, color=color)

sp.axhline(25, color='black', ls='--', label='Bunch spacing')
sp.legend(loc='upper left', bbox_to_anchor=(1,1), title='Em. angle [$\circ$]')

if args.o:
    plt.suptitle('')
    plt.subplots_adjust(hspace=0.4)
    plt.savefig(os.path.expanduser(args.o))

if not args.noshow:
    plt.show()

