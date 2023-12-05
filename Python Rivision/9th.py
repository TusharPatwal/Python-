# Modules

import converters as c

from converters import kg_to_lbs,lbs_to_kg

print(lbs_to_kg(210))

print(c.lbs_to_kg(154))

print(c.kg_to_lbs(70))

# function to find max number

def find_max(numbers):
    max = numbers[0]
    for number in numbers:
        if number > max:
            max = number
    print(max)

find_max([1,2,80,4,5,6])