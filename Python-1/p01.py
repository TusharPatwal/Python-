# This program performs simple arithmetic operations

num1 = float(input("Enter a number: "))
num2 = float(input("Enter another number: "))

print("\nMenu")
print("1 - Addition")
print("2 - Subtraction")
print("3 - Multiplication")
print("4 - Division")

choice = int(input("\nEnter your choice: "))

if choice == 1:
    result = num1 + num2
    print("\nThe result is", result)
elif choice == 2:
    result = num1 - num2
    print("\nThe result is", result)
elif choice == 3:
    result = num1 * num2
    print("\nThe result is", result)
elif choice == 4:
    result = num1 / num2
    print("\nThe result is", result)
else:
    print("\nInvalid choice. Please try again.")
