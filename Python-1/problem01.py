import os
# n = int(input("Enter the n: "))
d1 = {}
# for i in range(n):
bid_done = False
while not bid_done:
    name = input("Enter the name: ")
    bid = int(input("Enter the amount: "))
    d1[name] = bid
    bid_continue = input("Enter 'yes' if you want to continue the bid or 'no' if not: ")
    if bid_continue == 'no':
        bid_done = True
    elif bid_continue == 'yes':
        os.system('cls')
    
a = max(d1.values())
keys = [k for k, v in d1.items() if v == a]

print(keys)
