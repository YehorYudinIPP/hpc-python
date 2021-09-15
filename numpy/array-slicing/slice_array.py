import numpy as np

# 0)
a = np.random.rand(4,4)
print(a)

# 1)
b = a[1, :]
print(b)

# 2)
c = a[:, 2]
print(c)

# 3)
a[:2, :2] = 0.21
print(a)

# 4)
d = np.zeros((8,8))
d[::2, ::2] = 1
d[1::2, 1::2] = 1
print(d)

