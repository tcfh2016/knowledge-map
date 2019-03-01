from functools import reduce

def even(x):
  return x % 2 == 0

print(even(3))

print(list(map(even, range(10))))
print(list(map(lambda x: x % 2 == 0, range(10))))

print(list(filter(even, range(10))))
print(list(filter(lambda x: x % 2 == 0, range(10))))

print(reduce(lambda x, y: x + y, range(10)))
