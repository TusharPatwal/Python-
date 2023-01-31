# # cook your dish here

import random
import string

def generate_password(length):
    # Use the string library to get a list of all letters and digits
    characters = string.ascii_letters + string.digits
    # Use random.sample to choose `length` random elements from `characters`
    password = ''.join(random.sample(characters, length))
    return password

# Example usage:
password = generate_password(36)
print(password)
