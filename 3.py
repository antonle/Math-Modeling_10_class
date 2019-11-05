import matplotlib.pyplot as plt
import numpy as np
def cir(r=1,a=2,b=3):
    x = np.arange(-5,5,0.1)
    y = np.arange(-5,5,0.1)
    X,Y = np.meshgrid(x,y)
    fxy = X**2 + Y**2
    plt.contour(X,Y,fxy,levels=[r**2])
    fxy = X**2/a**2+Y**2/b**2
    plt.contour(X,Y,fxy,levels=[r**2])
    plt.title('окружность и элипс')
    plt.legend()
    plt.show()
    
    
cir(1)