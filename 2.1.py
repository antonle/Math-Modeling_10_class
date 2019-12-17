import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
t = np.arange(0, 10.01, 0.01)
def diff_func (z, t) :
    s, omega = z
    ds_dt = omega
    domega_dt = -g * np.sin(s / l)
    return ds_dt, domega_dt
s0 = 1
omega0 = 0
l = 4
g = 9.8
z0 = s0, omega0
solve = odeint(diff_func, z0, t)
plt.plot(t, solve[:, 0])
plt.axis('equal')
plt.show()