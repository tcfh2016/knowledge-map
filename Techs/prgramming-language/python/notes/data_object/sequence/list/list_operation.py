list_a = [1, 2, 3, 4, 5]
list_b = [2, 3, 4, 5, 6]

'''
print("list a + list b:")
print(list_a + list_b)
print("list a - list b:")
print(list_a - list_b)
'''

print([item for item in list_a if item not in list_b])

set_a = set([1, 2, 3, 4, 5])
set_b = {2, 3, 4, 5, 6}

print("set a + set b:")
print(set_a | set_b)
print("set a - set b:")
print(set_a - set_b)
