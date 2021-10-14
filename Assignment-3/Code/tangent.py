import numpy as np
import matplotlib.pyplot as plt

def lineX(x1,x2):
    x=np.linspace((4*x1-x2)/3,(4*x2-x1)/3,10)
    return x
def lineY(y1,y2):
    y=np.linspace((4*y1-y2)/3,(4*y2-y1)/3,10)
    return y
def circ(x,r):
    return np.sqrt(r*r-x*x)

r=3
A=[9/7,6*np.sqrt(10)/7]
B=[9/7,-6*np.sqrt(10)/7]
C=[-9/7,6*np.sqrt(10)/7]
D=[-9/7,-6*np.sqrt(10)/7]
P=[7,0]
Q=[-7,0]
O=[0,0]

plt.plot(O[0], O[1], 'o')
plt.text(-0.9,-0.9,'O',weight = "bold")
plt.plot(P[0], P[1], 'o')
plt.text(7,0.5,'P',weight = "bold")
plt.plot(Q[0], Q[1], 'o')
plt.text(-7,0.5,'Q', weight = "bold")
plt.plot(A[0], A[1], 'o')
plt.text(A[0]*(1.1),A[1]*(1.1),'A', weight = "bold")
plt.plot(B[0], B[1], 'o')
plt.text(B[0]*(1.2),B[1]*(1.2),'B', weight = "bold")
plt.plot(C[0], C[1], 'o')
plt.text(C[0]*(1.1),C[1]*(1.1),'C', weight = "bold")
plt.plot(D[0], D[1], 'o')
plt.text(D[0]*(1.2),D[1]*(1.2),'D', weight = "bold")

plt.plot(lineX(A[0],P[0]),lineY(A[1],P[1]),label="AP")
plt.plot(lineX(B[0],P[0]),lineY(B[1],P[1]),label="BP")
plt.plot(lineX(C[0],Q[0]),lineY(C[1],Q[1]),label="CQ")
plt.plot(lineX(D[0],Q[0]),lineY(D[1],Q[1]),label="DQ")
theta = np.linspace( 0 , 2 * np.pi , 150 ) 
a = r * np.cos( theta )
b = r * np.sin( theta ) 
plt.plot( a, b, label='Circle' )
plt.gca().set_aspect('equal')
plt.grid()
plt.legend(loc='best')
plt.axis([-9, 9, -6, 6])
plt.show()

