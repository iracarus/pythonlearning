spam = 'Hello World!'

print(spam.lower())
print(spam.upper())
print('hello world!'.title())
print(spam.isupper())
print(spam.islower())
print(spam.isalpha())   # letters only
print(spam.isalnum())   # letters and numbers only
print(spam.isdecimal()) # numbers only
print(spam.isspace())   # whitespace only
print(spam.istitle())   # titlecase only
print(spam.startswith('Hello'))
print(spam.endswith('World!'))

# join
print('\n\n'.join(['Rat', 'Bat', 'Mat']))

# split
print('My name is Raj'.split(' '))

#rjust
print('Hello'.rjust(20))
print('Hello'.rjust(20, '*'))

#ljust
print('Hello'.ljust(20))
print('Hello'.ljust(20, '*'))

# center
print('Hello'.center(20))
print('Hello'.center(20, '*'))

# strip, lstrip, rstrip
print('    X     '.strip())
print('    X     '.lstrip())
print('    X     '.rstrip())


# replace
spam = 'Hello There'
print(spam.replace('e', 'XYZ'))
