# example 1 : use of range
print('My name is')
for i in range(5):
    print('Jimmy five times' + str(i) )


# example 2 : find total of first 100 ints
total = 0
for num in range(101):
    total = total + num
print(total)


# example 3 : range again
print('My name is')
for i in range(12,15):
    print('Jimmy five times ' + str(i))

#example 4 : range with step argument
print('My name is')
for i in range(0, 10, 2):
    print('Jimmy five times ' + str(i))


# example 5 : negative step
print('My name is ')
for i in range(5, -1, -1):
    print('Jimmy five times ' + str(i))
