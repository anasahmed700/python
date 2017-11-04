# OBJECTS 1
class Dog():
    total = 0 # adding in object 5 step
    def __init__(self, name, age):
        print('dog init')
        print('name', name)
        print('age', age)
        self.name = name
        self.age = age
        Dog.total = Dog.total + 1 # adding in object 5 step

    def bark(self):
        print(self.name.title()+' is barking')

myDog = Dog('willie', 6)

# OBJECTS 2
print('\nOBJECTS 2')
print(myDog.name)
print(myDog.age)

# OBJECTS 3
print('\nOBJECTS 3')
myDog.bark()

# OBJECTS 4
print('\nOBJECTS 4')
yourDog = Dog('lucy', 4)

myDog.bark()
yourDog.bark()

# OBJECTS 5
print('\nOBJECTS 5')
print(Dog.total)

# OBJECTS 6 & 7 skip