import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.gca(projection='3d')

t = np.arange(0.01, 10 * np.pi, 0.01)

x = pow(2, -0.1 * t) * np.cos(t)
y = pow(2, -0.1 * t) * np.sin(t)
z = -t

ax.plot(x, y, z)

plt.show()
