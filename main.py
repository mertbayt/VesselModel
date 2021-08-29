import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import random
from scipy import integrate
import numexpr as ne

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

def f(x):
        return 3.75*((-((x*.2)*(x*.2)*(x*.2))-np.log(5)+2.5))

def g(x):
        return (-(np.square(x)*.175))

x = []
y = []
z = []

x1 = []
z1 = []

y2 = []

xR = []
zR = []

xR1 = []
zR1 = []

def Rz(w,l):
        return z[w]*np.cos(l)-x[w]*np.sin(l)

def Rx(w,l):
        return z[w]*np.sin(l)+x[w]*np.cos(l)

def Rz1(w,l):
        return z1[w]*np.cos(l)-x1[w]*np.sin(l)

def Rx1(w,l):
        return z1[w]*np.sin(l)+x1[w]*np.cos(l)

q = 0
a = 90
h = 0
m = 0
q = 0

for p in np.arange(0, 7.707, .01):

        x.append(p)

        z.append(0)

        if p > 1:
                x1.append(p)
                y.append(f(p))
                z1.append(0)
                xR1.append(Rz1(m, q))
                zR1.append(Rx1(m, q))
                q = q + 45
                m = m + 1

        y2.append(g(p))

        xR.append(Rz(h,a))
        zR.append(Rx(h,a))

        a = a + 45
        h = h +1


#ax.scatter(x, y, z, c='g', marker='o', label='f(x)')
#ax.scatter(x, y2, z, c='y', marker='o', label='g(x)')
ax.scatter(xR1, y, zR1, c='b', marker='o', label='r(f(x))')
ax.scatter(xR, y2, zR, c='r', marker='o', label='r(g(x))')

plt.legend(loc='upper left');

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

ax.set_zlim(-35, 35)
ax.set_xlim(-35, 35)
ax.set_ylim(-35, 35)

plt.show()