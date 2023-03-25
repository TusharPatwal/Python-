import os


operator = int(input("Enter the operator number(1 +, 2 -, 3 *, 4 /): "))



def calculator():
    number1 = eval(input("Enter the first number: "))
    number2 = eval(input("Enter the second number: "))
    while(True):
        if(operator == 1):
            print(number1+number2)
            break
        elif(operator == 2):
            print(number1-number2)
            break
        elif(operator == 3):
            print(number1*number2)
            break
        elif(operator == 4):
            print(number1/number2)
            break
        
calculator()

cal = input("Enter 'y' for continuing the program and 'n' for closing the program: ")


def check(cal):
    os.system("cls")
    if(cal=='y'):
        return calculator()
    else:
        return "The end!"


check(cal)