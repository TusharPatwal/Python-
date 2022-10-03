#[] = List
#{} = Set
#() = Tuple


#students = ["ram", "shyam", "kishna", "radha", "radhika"]

'''for student in students:
    if student == "radha":
        break #BREAK in python
    print(student)
'''

'''for student in students:
    if student == "kishna":
        continue #Continue in python
    print(student)
'''


## Tuple
'''marks = (95, 98, 97, 97, 97)
print(marks.count(97))
print(marks.index(98)) #.index shows the position of number [It always starts from {0-n}]
'''

## Set
'''marks = {95, 98, 97, 97, 97}
#print(marks)
for score in marks:
    print(score)
'''

## Dictionary
marks = {"English" : 95, "Chemistery" : 98}

print(marks["Chemistery"])

marks["physics"] = 97
print(marks)

print(marks["physics"])

marks["physics"] = 99
print(marks)
