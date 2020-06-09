import numpy as np

nd1 = np.array([[2,2,2], [4,4,4], [6,6,6]])
print(nd1)
print(type(nd1.shape))
print(nd1.shape)
print("nd1[1:] = ")
print(nd1[1:])
print("nd1[0:-1] = ")
print(nd1[0:-1])
print(nd1[1:] / nd1[0:-1])
