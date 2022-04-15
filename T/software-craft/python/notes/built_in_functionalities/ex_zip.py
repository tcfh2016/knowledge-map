keys = range(1, 5)
values = range(10, 41, 10)

tuple_list = zip(keys, values)
print(tuple_list)
print([pair for pair in tuple_list])

unzip_list = zip(*zip(keys, values))
print(unzip_list)
print([pair for pair in unzip_list])
