# Lists

names = ['tushar', 'bobby', 'ansh', 'krishna', 'sharthak']
print(names[2].capitalize())
print(names[2:4])

numbers = [1, 3, 4, 10, 7, 7, 8, 9]
MAX = numbers[0]
for number in numbers:
    if number > MAX:
        MAX = number
print(MAX)
# print(MAX(numbers))


# 2D lists
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix)

nums = [1, 2, 3, 2, 1, 3, 5, 6, 8, 6, 5, 9]
uniques = []
for number in nums:
    if number not in uniques:
        uniques.append(number)

print(uniques)
