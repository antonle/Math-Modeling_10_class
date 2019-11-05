import matplotlib.pyplot as plt
import numpy as np


def curve(a1=1,b1=1,c1=1,a2=1,k=1):
    """Рисует параболу и гиперболу"""
    x = np.arange(1,2,0.01)
    y1 = a1*x**2+b1*x+c1
    plt.plot(x,y1,label='парабола')
    x = np.arange(1,2,0.01)
    y2 = a2/(k*x)
    plt.plot(x,y2, label='гипербола')
    plt.title('гипербола и гипербола')
    plt.legend()
    plt.show()


curve(2,3,4,1,0.01)
    