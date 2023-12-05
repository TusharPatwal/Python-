# exception handling 

try:
    age = int(input('Age: '))
    income = 20000
    risk = income / age
    print(risk)
except ValueError:
    print('Invalid Value')
except ZeroDivisionError:
    print('Age cannot be 0')
finally:
    print('hello')

