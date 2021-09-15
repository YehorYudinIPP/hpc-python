import numpy as np

# 1)
a_l = [1, 2.0, 3.]
a = np.array(a_l)
print(a)

# 2)
b = np.arange(-2.0, 2.2, 0.2)
print(b)

# 3)
c = np.linspace(0.5, 1.5, 11)
print(c)

# 4)

c_s = 'abbcdf0_ RgG$'
c = np.array(c_s, dtype='c')
print(c)
print(c[3])


