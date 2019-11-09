import numpy as np

A=np.array([[1.5,0.5,0],[0,2,0],[0,0,0.5]])
B=np.linalg.inv(A)
print(A)
print(B)