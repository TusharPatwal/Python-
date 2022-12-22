import os
n = int(input("Enter the n: "))
d1 = {}
for i in range(n):
    name = input("Enter the name: ")
    bid = int(input("Enter the amount: "))
    d1[name] = bid
    os.system('cls')
    
a = max(d1.values())
keys = [k for k, v in d1.items() if v == a]

print(keys)
