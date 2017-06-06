from __future__ import division
import numpy as np
from scipy.constants import c

r = 22e-3
R = 2803.95


x = np.sqrt(2*R*r + r**2)
print 'x = %.2e' % x

Phi = np.tan(x/R)
Theta = x/R

print 'Phi, Theta: %.5e, %.5e' % (Phi, Theta)

print 'Path difference %r' % (R*(Phi - Theta)/c)

print 'Time needed to transverse chamber %r' % (2*r/c)

inc_angle_rad = (np.pi/2 - Phi)
print 'Incident angles relative to normal %r, in degrees %r' % (inc_angle_rad, inc_angle_rad/np.pi*180)

