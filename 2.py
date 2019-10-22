from const import g
from numpy import pi
import math
from const import e,k,h
h = 100
b = 30
a = 60
c = 1/math.tan(b)
d = c**2
e = 1/math.tan(a)
f = math.cos(a)
l = f**2
v1 = (g*h*d)/(2*l*(1-c*e)) 
v = math.sqrt(v1)
print(v)
print('-------------------------------------')
t = 200
e1 = 300
p = 2/math.sqrt(pi)
p1 = h/(k*t)**(3/2)
p2 = e**(-e1/(k*t))*e1**(t/2)
ans = p*p1*p2
print(ans)