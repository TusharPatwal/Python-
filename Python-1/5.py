first = input("enter first number : ")
operator = input("enter operator (+,-,*,/,%) : ")
second = input("enter second numdber : ")

first = int(first)
second = int(second)

if operator == "+":
    print(first + second)

elif operator == "-":
    print(first - second)

elif operator == "*":
    print(first * second)

elif operator == "/": 
    print(first / second)

elif operator == "%":
    print(first % second)

else : 
    print("saale daang se kam kar le")