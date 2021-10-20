import numpy as np
import matplotlib.pyplot as plt

n = np.linspace(-5,5,100)

x=np.cos(8*np.pi*1000*n)
plt.plot(n,x,label="$x(t)")
plt.grid()
plt.legend(loc='upper right')
plt.gca().set_aspect('equal')
plt.xlim(-5,5)
plt.ylim(-3,3)
plt.show()
