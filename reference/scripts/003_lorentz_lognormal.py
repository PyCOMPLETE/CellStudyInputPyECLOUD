from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import scipy.optimize as optimize

import LHCMeasurementTools.mystyle as ms

plt.close('all')
ms.mystyle()

def lorentz(xx, mu, sigma):
    return 1./(np.pi*sigma) * sigma**2/((xx-mu)**2 + sigma**2)


def lognormal(xx, mu, sigma):
    return stats.lognorm.pdf(xx, sigma, scale=np.exp(mu))


fig = ms.figure('Comparison of random functions for energy generation')


sp = plt.subplot(2,2,1)
sp.grid(True)


xx = np.linspace(0, 40, 1000)

yy_lorentz = lorentz(xx, mu=0.64, sigma=3.7)

fit_logn = optimize.curve_fit(lognormal, xx, yy_lorentz, p0=(0.64, 3.7))
yy_logn = lognormal(xx, mu=fit_logn[0][0], sigma=fit_logn[0][1])

sp.plot(xx, yy_lorentz, label='Lorentz')
sp.plot(xx, yy_logn, label='Lognormal')


sp.legend()

plt.show()

