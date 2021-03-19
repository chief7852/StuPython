import numpy as np

a = np.zeros((10,10),dtype=int)

b = np.ones(3,dtype=int)

print(a.shape)


b = np.reshape(a,(20,5))
print(b)