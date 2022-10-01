'''numbers = range(5)
print(numbers)
'''

'''i = 5
while i >= 0:
    print(i * "*" )
    i = i - 1
'''

'''for i in range(5):
    print(i + 1)
'''


'''marks = [95, 98, 97]
marks.append(99)
marks.insert(1, 93)
print(marks)

for score in marks :
    print(score)
    
print(93 in marks)
print(96 in marks)

print(len(marks))'''

marks = [95, 98, 97]

i = 0
while i < len(marks):
    print(marks[i])
    i = i + 1
    
marks.clear()
print(marks)