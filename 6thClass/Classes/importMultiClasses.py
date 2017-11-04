# from module import classes
from car import Car#, ElectricCar

mypasso = Car('toyota', 'passo', 2017)
print(mypasso.descriptive_name())

# myTesla = ElectricCar('tesla', 's4', 2017)
# print(myTesla.descriptive_name())


# importing all classes from a module
# from module_name import *
from car import *


# import an entire module
# import module_name
import car


# Importing a Module into a Module
from electric_car import ElectricCar
newTesla = ElectricCar('tesla', 's5', 2017)
print(newTesla.descriptive_name())