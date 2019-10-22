from const import g
import numpy as np
x0 = 0 
y0 = 0
v0 = 10
A = np.ndarray(shape=(6,3))
for t in np.arange(0,6,1):
    x = x0  + v0*t
    y = y0 + v0*t - (g*t**2)/2
    A[t,0] = t
    A[t,1] = x
    A[t,2] = y
print(A)
    
    
    
    