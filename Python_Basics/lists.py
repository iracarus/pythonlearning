spam = ['cat', 'bat', 'hat', 'mat'] # define list
print(spam[0]) #access list item

print('*************************************************')
spam[1] = 'chat'  # reassigning a value
print(spam[1])

print('*************************************************')
spam = spam + ['rat']   # adding new element
print(spam)

print('*************************************************')
# slicing
print(spam[1:3])
print(spam[:3])
print(spam[3:])

print('*************************************************')
# removing an element
del spam[2]
print(spam)

print('*************************************************')
# length of list
print(len(spam))

print('*************************************************')
# converting to list
stringValue  = 'Hello'
convValue = list(stringValue)
print(convValue)

print('*************************************************')
# conditional operator with lists
col = ['Raj', 'Manisha', 'Prateek', 'Birmu']
print('Prateek' in col) # True
print('Nari' in col) # False
print('Anubhav' not in col) # True


print('*************************************************')
# lists in loops
spam = ['Hat', 'Mat', 'Rat', 'Cat']
for i in range(len(spam)):
    print(spam[i])
