# importing classes
#from file import class
from car import Car

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.descriptive_name())

my_new_car.odometerReading = 23
print(my_new_car.get_odometer())


print('\nIMPORTING ELECTRIC CAR')
#from file import class
from car import ElectricCar
myTesla = ElectricCar('tesla', 's4', 2017)

print(myTesla.descriptive_name())

myTesla.battery.describe_battery()

myTesla.battery.get_range()