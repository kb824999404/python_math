import numpy as np
a=np.arange(100)
print(a[::10])
b=np.delete(a,np.arange(a.shape[0])[::10])
print(b)