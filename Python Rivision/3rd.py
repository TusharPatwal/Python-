# for loops

for name in ['tushar', 'ansh', 'krishna']:
    print(name)

prices = [10,20,30]

total = 0
for price in prices:
    total += price
print(f"Total: {total}")


for x in range(4):
    for y in range(3):
        print(f'({x},{y})')

numbers = [5,2,5,2,2]

for i in numbers:
    print('x'*i)