# Tested for 
# https://www.sathyabama.ac.in/sites/default/files/course-material/2020-10/UNIT3_1.pdf

from fftFromScratch import *

import matplotlib.pyplot as plt
x=np.array([1,1,1])

plt.stem(x,label='$x[n]$')
plt.grid()
plt.legend()
plt.show()

X=fft(x.T,4)
plt.stem(np.abs(X),label='|X[k]|')
plt.grid()
plt.legend()
plt.show()

plt.stem(np.angle(X),label='∠X[k]')
plt.grid()
plt.legend()
plt.show()
