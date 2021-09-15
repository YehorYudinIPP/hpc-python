import numpy as np
from matplotlib import pyplot as plt

dat = np.loadtxt('points_circle.dat')
#print(dat)

vector = (2.1, 1.1)
dat_translated = dat + vector
#print(dat_translated)

plt.plot(dat[:, 0], dat[:, 1], 'ro', label='original circle')
plt.plot(dat_translated[:, 0], dat_translated[:, 1], 'bo', label='translated circle')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='best')
plt.axis('equal')
plt.savefig('circles.png')

