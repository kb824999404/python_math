import numpy as np
A=np.loadtxt('mix_2.txt')
B=np.linalg.svd(A,full_matrices=False)
v=B[1]
for i in range(len(v)-1):
    print(v[i]/v[i+1])
