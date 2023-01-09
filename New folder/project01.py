import os
import pickle

# for inserting new student data to binary file
def addRecord():
    f = open("StudentData.txt","ab")
    student = {}
    rno = int(input("Enter Roll no.: "))
    name = input("Enter the name: ")
    course = input("Enter the course: ")
    sec = input("Enter the section: ")
    dob = input("Enter your date of birth: ")
    tMarks = int(input("Enter the total marks: "))
    
    # creating a dictionary to hold students data
    # student = {"RollNo":rno,"Name":name,"Course":course,"Section":sec,"DateOfBirth":dob,"TotalMarks":tMarks}
    
    student["Roll"] = rno
    student["Name"] = name
    student["Course"] = course
    student["Section"] = sec
    student["DateOfBirth"] = dob
    student["TotalMarks"] = tMarks
    
    
    # writing this record to file
    
    pickle.dump(student, f)
    f.close()
    print("New student Record is added successfully to file.")
    
# for reading the record of file
def displayRecord():
    f = open("StudentData.txt", "rb")
    while True:
        try:
            student = pickle.load(f)
            print(student)
        except EOFError:
            print("\nFile Read Completed. No further Records found")
            break
    f.close()
    
# for searching a record through rollno in file
def searchRecord():
    f = open("StudentData.txt", "rb")
    found = 1
    try:
        r = int(input("Enter the roll number: "))
        while True:
            student = pickle.load(f)
            if r == student["Roll"]:
                print(student)
                f = 0
    except EOFError:
        f.close()
    

# for updating marks in file with rollno
def updateMarks():
    f = open("StudentData.txt", "rb")
    
    # list variable to hold all records of student file
    studentLst = []
    while True:
        try:
            student = pickle.load(f)
            studentLst.append(student)
        except EOFError:
            break
    f.close()
    
    for i in range(len(studentLst)):
        if studentLst[i]["Roll"]==r:
            studentLst[i]["TotalMarks"]=m
            
    f = open("StudentData.txt", "wb")
    for x in studentLst:
        pickle.dump(x, f)
    print("Marks Updated Successfully.")
    f.close()
    

# for deleting a record from file
def deleteRecord():
    f = open("StudentData.txt", "rb")
    
    # list variable to hold all records of student file
    studentLst = []
    while True:
        try:
            student = pickle.load(f)
            studentLst.append(student)
        except EOFError:
            break
        f.close()
        ans = input("Are you sure to delete student record permanently?(Y/y for YES)")
        if ans == "y" or ans == "Y":
            f = open("StudentData.dat", "wb")
            for x in studentLst:
                if x["Roll"] == r:
                    continue
                pickle.dump(x, f)
            print("Student Record Deleted successfully.")
            f.close()


while True:
    print("\nType 1 to add new student data to file.")
    print("Type 2 to display all student data of file.")
    print("Type 3 to search a student data in file.")
    print("Type 4 to update student marks in file.")
    print("Type 5 to delete student record")
    
    choice = int(input("Enter your choice: "))
    if choice == 1:
        addRecord()
    elif choice == 2:
        displayRecord()
    elif choice == 3:
        searchRecord()
    elif choice == 4:
        updateMarks()
    elif choice == 5:
        deleteRecord()
    else:
        break