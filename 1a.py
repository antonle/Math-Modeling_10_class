import matplotlib.pyplot as plt
import numpy as np
alpha = np.arange(-2*np.pi, 2*np.pi, 0.1)
radius = 3
x = radius * (alpha - np.sin(alpha))
y = radius * (1 - np.cos(alpha))
plt.plot(x, y)
plt.xlim(-20, 20)
plt.ylim(-10, 10)
plt.show()
