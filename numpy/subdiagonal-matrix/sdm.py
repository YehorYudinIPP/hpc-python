import numpy as np

n = 6

A = np.eye(n, n, 1) + np.eye(n, n, -1)

print(A)

