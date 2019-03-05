import numpy as np

np.random.seed(1000)
y1 = np.random.standard_normal(20)
print(y1)
print(y1.cumsum())

y2 = np.array([[1,2,3], [4,5,6]])
print(y2)
print(y2.cumsum())
print(np.cumsum(y2))
# array([ 1,  3,  6, 10, 15, 21])

print(np.cumsum(y2, axis=0))
# 纵向累加
#[[1 2 3]
# [5 7 9]]

print(np.cumsum(y2, axis=1))
# 横向累加
#[[ 1  3  6]
# [ 4  9 15]]
