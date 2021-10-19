import numpy as np
import matplotlib.pyplot as plt

t1=np.linspace(-1,3,5)

x=[0,0,1,0,0]
h=[0,2,1,0,0]

y=np.convolve(x,h)

# the lower limit would change to -1+(-1)=-2, the upper limit would change to 3+3=6
t2=np.linspace(-2,6,9)
print(y)
plt.stem(t2,y,use_line_collection=True)
plt.ylabel('$y$')
plt.xlabel('$n$')
plt.show()