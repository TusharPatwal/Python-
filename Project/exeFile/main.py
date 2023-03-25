import os

def check():
    cal = input("Enter 'y' for continuing the program and 'n' for closing the program: ")
    os.system("cls")
    while(cal!='n'):
        return calculator()

def calculator():
    operator = int(input("Enter the operator number(1 +, 2 -, 3 *, 4 /): "))
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
        else:
            print("Error")
    
    return check()
    
calculator()