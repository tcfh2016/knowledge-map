l = [1, 3, 2]
iter = iter(l)
print(iter.__next__())
print(iter.__next__)
print(next(iter))

f = open('test-data.txt')
print(f.__next__())
print(next(f))
