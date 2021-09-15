import numpy as np

dx = 0.1
a = 0.
b = np.pi/2.
x = np.arange(a, b, dx)

y1 = np.sin(x)
y2 = np.cos(x)

dy1 = (y1[2:] - y1[:-2])/ (2.*dx)

#print(y1)
#print(y2)

rmse = np.sqrt(((y2[1:-1] - dy1)**2).mean())
print("RMSE = {0}".format(rmse))

