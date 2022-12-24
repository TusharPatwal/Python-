# add
def add(a, b):
    return a + b


# subtract
def subtract(a, b):
    return a - b


# multiply
def multiply(a, b):
    return a * b


# divide
def divide(a, b):
    return a / b


# dictionary
operations = {"+": add, "-": subtract, "*": multiply, "/": divide}
def calculator():
  num1 = eval(input("Whats's the first number: "))
  
  for i in operations:
      print(i)
  
  should_continue = True
  while should_continue:
    operation_symbol = input("Pick the operation you want to perform: ")
    num2 = eval(input("What's the second number: "))
  
  
    function = operations[operation_symbol]
    ans = function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {ans}")

    var = input(f"Type 'y' to continue calculating with {ans}, or type 'n'to start new calculation: ")
    
    if var == 'y':
      num1 = ans
    elif var == 'n':
      should_continue = False
      calculator()
    else:
      exit()

calculator()