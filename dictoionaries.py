myCat = { 'size' : 'fat', 'color' : 'gray', 'disposition' : 'loud'}
print(myCat['size'])

print('My cat has ' + myCat['color'] + ' fur.')

print('*******************************************')

# dictionaries are unordered
print([1,2,3] == [3,2,1]) # order matters in lists

eggs = {'name' : 'Zophie', 'species' : 'cat', 'age' : 8}
ham = {'species' : 'cat', 'name' : 'Zophie', 'age' : 8}

print(eggs == ham)


print('*******************************************')
# not in - in usage
print('name' in eggs)
print('name' not in eggs)
