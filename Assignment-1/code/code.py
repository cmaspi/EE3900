'''
Author: Chirag
EE3900
Assignment-1 Vectors 
'''
import numpy as np
import matplotlib.pyplot as plt
x=np.array([1,2,-2])
y=np.array([5,3,-11])


fig,ax=plt.subplots()
for i in range(3):
    ax.scatter(x[i],y[i])
    ax.annotate(chr(65+i),(x[i],y[i]),(x[i]-0.07,y[i]+0.35))
plt.plot(np.array([1,2]),np.array([5,3]), 'b', label="$AB$")
plt.plot(np.array([2,-2]), np.array([3,-11]),'r', label="$BC$")
plt.plot(np.array([1,-2]), np.array([5,-11]),'g', label="$CA$")
plt.xlim(-3,3)
plt.ylim(-14,7)

plt.legend(loc='lower right')
plt.show()
