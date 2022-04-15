d1 = {'a':1, 'b':3, 'c':2}
for key in d1.keys():
    print(key, d1[key])

d2 = {'a':1, 'b':3, 'c':2}
i = iter(d2)
print(next(i))
print(next(i))

d3 = {'e':1, 'f':3, 'g':2}
for key in d3:
    print(key, d3[key])
