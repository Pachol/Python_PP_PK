import numpy as np

print "put size of the matrix"

size = int(raw_input())
A = np.random.rand(size,size)
determinant = np.linalg.det(A)
print determinant