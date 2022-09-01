import pandas as pd

a = [1, 7, 2, 3]

myvar = pd.Series(a, index = ["w", "x", "y", "z"])
print(myvar)

print(myvar[0])
print(myvar['w'])
