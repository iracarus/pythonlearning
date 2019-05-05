# index - zero based
spam = ['Raj', 'Manisha', 'Prasidh', 'Arya', 'Jon']
print(spam.index('Prasidh'))

print('*******************************************')

# append - add value to end
spam.append('Ankit')
print(spam)

print('*******************************************')

# insert - add in between
spam.insert(2, 'Dany')
print(spam)

print('*******************************************')

# remove - remove an element
spam.remove('Dany')
print(spam)

print('*******************************************')
# difference between del and remove
# del - remove from index , remove - removes the chosen value
del spam[1]
print(spam)

print('*******************************************')
# remove only removes the first occurance
spam.append('Dany')
spam.insert(2, 'Dany')
spam.insert(4, 'Dany')
print(spam)
spam.remove('Dany')
print(spam)

print('*******************************************')
# sorting
spam = [2,5,4,1,-3]
spam.sort()
print(spam)

wham = ['Raj', 'Manisha', 'Prasidh', 'Birmu']
wham.sort()
print(wham)

# sort in reverse order
spam.sort(reverse=True)
print(spam)

print('*******************************************')
spam = [1, 2, 3 , 'Raj', 'Baj', 4]
# spam.sort() - TypeError - unorderable types
print('Nothing to print as it is errorneous')
print('*******************************************')
# sorting is ASCII-betical by default ( meanning that upper case comes before lower case)
spam = ['Raj', 'raj', 'manisha', 'Manisha']
spam.sort()
print(spam)

# sort in true alphabetical order
spam.sort(key=str.lower)
print(spam)
