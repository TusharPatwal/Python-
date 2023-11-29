# name = input("What's your name? ")
# favourite_color = input("Which colour do you like? ")
#
# print(name + " likes "+ favourite_color)

# birth_year = int(input("Birth year: "))
#
# age = 2023 - birth_year
#
# print(age)

# weigth_kgs = int(input("Enter your weight in kgs: "))
# weigth_lbs = weigth_kgs/0.45
# print(weigth_lbs)

# main = '''
# Hello everyone,
#
# This is Tushar Patwal
# Thankyou
# '''
# print(main)


# formatted string
#
# first = 'Tushar'
# last = 'Patwal'
# msg = f'{first} [{last}] is a coder'
# # print(msg)
#
#
# print(len(msg))
# print(msg.upper())
# print(msg.lower())


# Weight converter program

weight = eval(input("Enter Weight: "))
unit = input("(L)bs or (k)g: ")

if unit.lower() == 'k':
    print(f"You are {round(weight/.45, 2)} pounds.")
elif unit.lower() == 'l':
    print(f"You are {round(weight * .45, 2)} kg.")
else:
    print('Unit Error')