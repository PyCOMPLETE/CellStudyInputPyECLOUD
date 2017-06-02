from __future__ import division
import numpy as np
from scipy.constants import c

r = 22e-3
R = 2803.95


x = np.sqrt(2*R*r + r**2)
print 'x = %.2e' % x

Phi = np.tan(x/R)
Theta = x/R

print '%.5e %.5e' % (Phi, Theta)

print R*(Phi - Theta)/c

print 2*r/c

