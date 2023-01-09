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
    
