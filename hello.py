# This program says hello and asks for my AuthorName

print('Hello World!')

print('What is your name?') # ask for their Name
myName = input()
print('It is good to meet you, ' + myName)
print('The length of your name is :')
print(len(myName))

print('What is your age?') # ask for their age
myAge = input()
print('You will be ' + str(int(myAge)+1) + ' in a year.')
