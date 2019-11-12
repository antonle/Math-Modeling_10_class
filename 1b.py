import matplotlib.pyplot as plt
import numpy as np
alpha = np.arange(-2*np.pi, 2*np.pi, 0.1)
radius = 3
y = radius * np.sin(alpha)**3
x = radius * np.cos(alpha)**3
plt.plot(x, y)
plt.xlim(-20, 20)
plt.ylim(-10, 10)
plt.show()
