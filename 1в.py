import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.gca(projection='3d')

t = np.arange(0.01, 8 * np.pi, 0.01)
r = 2

x = r * np.cos(t) ** 3
y = r * np.sin(t) ** 3
z = np.cos(2 * t)

ax.plot(x, y, z)

plt.show()
