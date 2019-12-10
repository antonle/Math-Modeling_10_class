import numpy as np 
from scipy.integrate import odeint
import matplotlib.pyplot as plt
t = np.arange(0, 1000, 1)
def bacteria(m, t):
    dmdt = k * m
    return dmdt
m = 1
k = 0.0032
solve = odeint(bacteria, m, t)
plt.plot(t, solve)
plt.show()
