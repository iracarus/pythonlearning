import pprint

message = 'Quick brown fox jumped over the fence'
count = {}
for character in message.upper():
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count)

print('*******************************')

rjtext = pprint.pformat(count)
print(rjtext)
