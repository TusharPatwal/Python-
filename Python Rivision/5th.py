# tuple

coordinates = (1, 2, 3)

# unpacking
x, y, z = coordinates
print(x, y, z)

# dictionaries
customer = {
    'name': 'Tushar Patwal',
    'age': 21,
    'is_verified': True
}

print(customer['name'])
print(customer['age'])
print(customer['is_verified'])
print(customer)

# phone = input('Phone: ')

digits_mapping = {
    '1': 'One',
    '2': 'Two',
    '3': 'Three',
    '4': 'Four',
    '5': 'Five',
    '6': 'Six',
    '7': 'Seven',
    '8': 'Eight',
    '9': 'Nine',
    '0': 'Zero'
}

message = input('> ')
words = message.split(' ')
emojis = {
    ':)': '😊',
    ':(': '😒'
}

output = ''
for word in words:
    output += emojis.get(word, words) + ' '

print(output)
