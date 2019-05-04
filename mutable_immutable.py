import copy

#
spam = [0,1,2,3,4]
cheese = spam
cheese[1] = 'Hello'
print(cheese)
print(spam) # spam is also changed because the reference is same

print('*************************************')

# functions arguments having lists
def eggs(cheese):
    cheese.append('Hello')

spam = [1,2,3]
eggs(spam)
print(spam)

print('*************************************')
# deepcopy
spam = ['A', 'B', 'C', 'D']
cheese = copy.deepcopy(spam)
cheese[1] = 42
print(cheese)
print(spam)
