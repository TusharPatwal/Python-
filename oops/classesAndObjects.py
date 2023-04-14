class students:
    id = 98
    name = 'tushar'

    def display(self):
        print(self.id, self.name)
        print("ID: %d \nName: %s" % (self.id, self.name))
# student = students()
# student.display()


if __name__ == '__main__':
    s = students()    
    s.display() 