from scipy.fft import fft

# input signal
x= [1,0,2,3]
# fast fourier transform
X=fft(x)
print(X)