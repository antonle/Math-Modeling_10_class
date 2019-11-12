import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
fig, ax = plt.subplots()
anim_object, = plt.plot([], [], 'o')
xdata, ydata = [], []
ax.set_xlim(-4, 4)
ax.set_ylim(-3, 3)
def update(frame):
    r = 3
    xdata.append(r * np.cos(frame)**3)
    ydata.append(r * np.sin(frame)**3)
    anim_object.set_data(xdata, ydata)
    return anim_object, 
ani = FuncAnimation(fig,
                    update,
                    frames = np.arange(-2*np.pi, 2*np.pi, 0.1),
                    interval = 300)
ani.save('ani.gif')
