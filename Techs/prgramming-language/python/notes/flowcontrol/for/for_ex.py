set1 = [1, 2, 3, 4, 5]
set2 = [3, 5]

print("1. simple and direct way")
for c in set1:
    if c not in set2:
        print(c)

print("2. using lambda")
print([x for x in set1 if x not in set2])

print("3. using generator")
gen = (x for x in set1 if x not in set2)
for x in gen:
    print(x)

print("4. using filter")
for x in filter(lambda x:x not in set2, set1):
    print(x)
