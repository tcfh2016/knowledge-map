l = [1, 3, 2]
iter = iter(l)
print(iter.__next__())
print(iter.__next__)
print(next(iter))

f = open('test-data.txt')
print(f.__next__())
print(next(f))

x = 0

map(lambda x : print(x), [y for y in [1,2,3]])

def func(x):
    x = 2
res = map(func, [y for y in range(5)])
print(list(res))

print(x)
