'''
Author: Chirag
EE3900
Assignment-1 Vectors
'''
import numpy as np
import matplotlib.pyplot as plt
from sympy.matrices import Matrix

# x coords of input
x=np.array([1,2,-2])
# y coords of input
y=np.array([5,3,-11])

input=np.array([x,y])

# input as a matrix
input=input.reshape(2,3)

#Making the M matrix
M=Matrix([input[:,1]-input[:,0],input[:,2]-input[:,0]])
# verifing M with what was calculated in tex file
print(M)

# taking rref of M matrix
M_rref = M.rref()
print("The reff of matrix M is given as : ",M_rref)


fig,ax=plt.subplots()
for i in range(3):
    ax.scatter(x[i],y[i])
    ax.annotate(chr(65+i),(x[i],y[i]),(x[i]-0.07,y[i]+0.35))
plt.plot(np.array([1,2]),np.array([5,3]), 'b', label="$AB$")
plt.plot(np.array([2,-2]), np.array([3,-11]),'r', label="$BC$")
plt.plot(np.array([1,-2]), np.array([5,-11]),'g', label="$CA$")
plt.grid()
plt.xlim(-3,3)
plt.ylim(-14,7)
plt.legend(loc='lower right')
plt.show()
