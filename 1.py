import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
t = np.arange(0, 10, 0.1)
def diff_func(z, t) :
    x, v_x, y, v_y = z
    dxdt = v_x
    dvxdt = (np.sin(np.pi / 6) * f2 + np.cos(np.pi / 6) * f3 + f4) / m
    dydt = v_y
    dvydt = (np.cos(np.pi / 6) * f2 + np.sin(np.pi / 6) * f3 + f1) / m
    return dxdt, dvxdt, dydt, dvydt

m = 1
f1 = 10
f2 = 10
f3 = 10
f4 = 10

x0 = 0
y0 = 0
v_x0 = 0
v_y0 = -100000000000

z0 = x0, v_x0, y0, v_y0
solve = odeint(diff_func, z0, t)

plt.plot(solve[:, 0], solve[:, 2])
plt.show()
    
    
    