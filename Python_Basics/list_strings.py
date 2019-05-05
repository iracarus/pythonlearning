# String can be directly taken into a list
l = list('Hello') # if used [] we get TypeError - 'type' object is not subscriptable
print(l)

print('****************************************')

# index can be used with strings
name = 'Sophie'
print(name[0])
print(name[1:3]) # slicing also works
print(name[-3]) # can be used for reversing

print('op' in name) # true
print('jo' in name) # False

print('****************************************')
# lists are mutable
for letter in name:
    print(letter)

# Strings are immutable
name = 'Sophie the cat'
print(name[3]) # indexed values can be accessed
# name[2] = 'o' - cannot be reassinged
# throws error as TypeError - 'str' object does not support item assignment

print('****************************************')
# HOW TO CHANGE String
name = 'Sophie a cat'
newName = name[0:7] + 'the' + name[8:12] # length of 'Sophie '- 7,
print(newName) 
