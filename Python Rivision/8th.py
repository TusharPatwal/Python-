# classes

class Point:

    # Constructor
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def move(self):
        print('move')

    def draw(self):
        print('draw')


class Person:

    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f'Hi, I am {self.name}')


class Animal:
    def walk(self):
        print('walk')


# inheritance
class Dog(Animal):
    pass


# inheritance
class Cat(Animal):
    pass

if __name__ == "__main__":
    point = Point(10,20)
    point.draw()
    print(point.x)

    person = Person('tushar')
    person.talk()

    cat = Cat()
    cat.walk()

    dog = Dog()
    dog.walk()