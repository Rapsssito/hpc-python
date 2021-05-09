import numpy as np

A = np.random.rand(2,2)
A = A + A.T
print(A)
B = np.random.rand(2,2)
B = B + B.T
print(B)

C = np.dot(A, B)
print(C)

eigs = np.linalg.eigvals(C)
print("Eigenvalues are: " + str(eigs))