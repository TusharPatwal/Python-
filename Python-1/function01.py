# types of function argunments in python

# default arguments
def add(a = 4,b = 1,c = 3):
    '''Assign default values to argunment using '=' operator at the time of function defination'''

    return (a+b+c)

print(add())


# positional argument
def subtract(a,b,c):
    '''Values get assigned as per the sequence'''
    return (a-b-c)

print(subtract(10, 4, 1))


# keyword arguments
def multiply(a,b,c):
    '''Arguments where values get assigned to the arguments by their keyword'''
    return (a*b*c)

print(multiply(c=2,a=8,b=5))


# arbitrary positional arguments
def wholeSum(*a):
    '''An asterisk (*) is placed before a parameter in function definition which can hold non-keyword variable-length arguments'''
    result = 0
    for i in a:
        result += i
    return result

print(wholeSum(1,2,3,4,5,6,7,8,9,10))


# arbitrary keyword arguments
def dictionary(**a):
    '''double asterisk (**) is placed before a parameter in a function which can hold keyword variable-length arguments'''
    for i in a.items():
        print(i)

dictionary(rollno=98,name='Tushar',course='BCA')