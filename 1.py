import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
t = np.arange(0, 10.01, 0.01)
def diff_func (z, t) :
    y, omega = z
    dy_dt = omega
    domega_dt = np.sin(y) - omega - 3 * y * t - 5
    return dy_dt, domega_dt
y0 = 0.01
omega0 = 0.5
z0 = y0, omega0
solve = odeint(diff_func, z0, t)
plt.plot(solve[:, 1], solve[:, 0])
plt.show()