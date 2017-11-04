# Question 5:
# Define a class named Shape and its subclass Square. The Square class
# has an init function which takes a length as argument. Both classes
# have a area function which can print the area of the shape where
# Shape's area is 0 by default.
# Hints:
# To override a method in super class, we can define a method with the
# same name in the super class.

class shape():
    area = 0
    def __init__(self, length):
        self.length = length

class square(shape):
    def area(self):
        a = (self.length*self.length)
        print('the area of a square with a side length of %f is %f' % (self.length, a))

s = square(5)
s.area()
