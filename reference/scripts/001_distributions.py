from __future__ import division
import os
import argparse
import numpy as np
import scipy.integrate as integrate
import scipy.stats as stats
import matplotlib.pyplot as plt

import LHCMeasurementTools.mystyle as ms
plt.close('all')
ms.mystyle(12)

parser = argparse.ArgumentParser()
parser.add_argument('-o')
parser.add_argument('--noshow', action='store_true')
args = parser.parse_args()

sig = 5
mu = 7

x0 = 0.64
gamma = 3.7

sig2 = np.sqrt(np.log(sig**2/mu**2 +1))
mu2 = np.log(mu) - sig2**2/2

fig = ms.figure('Distributions')

sp = plt.subplot(2,2,1)
sp.grid(True)
sp.set_xlabel('Energy [eV]')

def gauss(xx):
    return 1/(np.sqrt(2*np.pi*sig**2)) * np.exp(-(xx-mu)**2/(2*sig**2))

def cauchy(xx):
    return stats.cauchy.pdf(xx, x0, gamma)

def lognormal(xx):
    return 1/(xx*sig2*np.sqrt(2*np.pi))*np.exp(-(np.log(xx)-mu2)**2/(2*sig2**2))

def rect(xx):
    out = np.zeros_like(xx)
    mask = np.logical_and((mu - sig/2) < xx,xx < (mu + sig/2))
    out[mask] = 1/sig
    return out



xx_plot = np.linspace(0.1,30,1000)

func_titles = [(gauss, 'Truncated gaussian'),
               (lognormal, 'Log-normal'),
               (cauchy, 'Lorentz'),
               (rect, 'Rectangular'),
               ]

for ctr, (func, title) in enumerate(func_titles):
    color = ms.colorprog(ctr, func_titles)
    if func is rect:
        norm = 1
    else:
        norm = integrate.quad(func, 0, np.inf)[0]
    yy_plot = func(xx_plot) / norm
    sp.plot(xx_plot, yy_plot, label=title, color=color)
    #if title != 'Lorentz':
    #    mean = integrate.quad(lambda x: x*func(x), 0, np.inf)[0] / norm
    #    sp.axvline(mean, color=color)

sp.legend(loc='upper right')


sp = plt.subplot(2,2,2)
sp.grid(True)
sp.set_xlabel('Angle [rad]')

xx = np.linspace(0,np.pi/2, 1000)
yy = np.cos(xx) / integrate.quad(np.cos, 0, np.pi/2)[0]
yy2 = np.sin(xx)*np.cos(xx)/ integrate.quad(lambda x: np.sin(x)*np.cos(x), 0, np.pi/2)[0]

sp.plot(xx, yy, label=r'$\cos\theta$')
sp.plot(xx, yy2, label=r'$\cos\theta\sin\theta$')

sp.legend(loc='upper right')


if args.o:
    plt.suptitle('')
    plt.savefig(os.path.expanduser(args.o))

if not args.noshow:
    plt.show()

