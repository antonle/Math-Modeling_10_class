import numpy as np

def multi(A):
     """Функция, которая перемножает все элементы массива"""
     s = 1
     for i in range(0,len(A),1):
         s = s * A[i]
         print(s)
     return(s)
     
A = np.arange(1,11,1)
print(multi(A))