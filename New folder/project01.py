import os

# for inserting new student data to binary file
def addRecord():
    import pickle
    rno = int(input("Enter Roll no.: "))
    name = input("Enter the name: ")
    course = input("Enter the course: ")
    sec = input("Enter the section: ")
    dob = input("Enter your date of birth: ")
    tMarks = int(input("Enter the total marks: "))
    
    # creating a dictionary to hold students data
    student = {"RollNo":rno,"Name":name,"Course":course,"Section":sec,"DateOfBirth":dob,"TotalMarks":tMarks}
    
    # writing this record to file
    f = open("StudentData.dat","ab")
    pickle.dump(student, f)
    f.close()
    print("New student Record is added successfully to file.")
    
# for reading the record of file
def displayRecord():
    import pickle
    f = open("StudentData.dat", "rb")
    while True:
        try:
            stu = pickle.load(f)
            print("Roll No: ", stu[RollNo])
            print("Name: ", stu[Name])
            print("Course: ", stu[Course])
            print("Section: ", stu[Section])
            print("Date of birth: ", stu[DateOfBirth])
            print("Total Marks: ",stu[TotalMarks])
        except EOFError:
            print("\nFile Read Completed. No further Records found")
            break
    f.close()
    
# for searching a record through rollno in file
def searchRecord(r):
    import pickle
    f = open("StudentData.dat", "rb")
    found = False
    while True:
        try:
            student = pickle.file(f)
            if student["RollNo"] == r:
                print("Roll No: ", stu[RollNo])
                print("Name: ", stu[Name])
                print("Course: ", stu[Course])
                print("Section: ", stu[Section])
                print("Date of birth: ", stu[DateOfBirth])
                print("Total Marks: ",stu[TotalMarks])
                found = True
        except EOFError:
            break
    if found == False:
        print(f"No student record found with{r} Roll Number")
    f.close()
    

# for updating marks in file with rollno
def updateMarks(r,m):
    import pickle
    f = open("StudentData.dat", "rb")
    
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
        if studentLst[i]["RollNo"]==r:
            studentLst[i]["TotalMarks"]=m
            
    f = open("StudentData.dat", "wb")
    for x in studentLst:
        pickle.dump(x, f)
    print("Marks Updated Successfully.")
    f.close()
    

# for deleting a record from file
def deleteRecord(r):
    import pickle
    f = open("StudentData.dat", "rb")
    
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
                if x["RollNo"] == r:
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
    