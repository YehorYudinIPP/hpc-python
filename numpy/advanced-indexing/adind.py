import numpy as np

n = 10
A = np.random.rand(n, n)
print(A)

thr = 0.5
mask = A > thr
print(mask)
print(A[mask])

mask_inds = np.nonzero(mask)
print(mask_inds)

