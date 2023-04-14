# Python Constructor
# A constructor is a special type of method which is used to intialize the instance members of the class.

# types of constructor:
#                      1. Parameterized Constructor
#                      2. Non-parameterized Constructor

class Employee:
    def __init__(self, name, id):  
        self.id = id  
        self.name = name  
        
    def display(self):
        print("ID: %d \nName: %s" % (self.id, self.name))
        

emp1 = Employee("Tushar", 98)
emp2 = Employee("Ansh", 79)

emp1.display()
emp2.display()
    
    
# Non-Parameterized Constructor
class Student:  
    def __init__(self):  
        print("This is non parametrized constructor")  
    def show(self,name):  
        print("Hello",name)  
        
student = Student()  
student.show("John") 


# Parameterized Constructor
class Student:  
    def __init__(self, name):  
        print("This is parametrized constructor")  
        self.name = name  
    def show(self):  
        print("Hello",self.name)  

student = Student("John")  
student.show()    