# there are 3 methods for dictionaries - keys, values, items

eggs = {'name' : 'Zophie', 'species' : 'cat', 'age' : 8}
# 1. keys
print(list(eggs.keys()))
print(eggs.keys())
print('*****************************************')

# 2. values
print(list(eggs.values()))
print(eggs.values())
print('*****************************************')

# 3. items
print(list(eggs.items()))
print(eggs.items())
print('*****************************************')

# using for loops
for k in eggs.keys():
    print(k)

for v in eggs.values():
    print(v)

for k,v in eggs.items():
    print(k,v)

for i in eggs.items():
    print(i)    # i acts like a object reference here
