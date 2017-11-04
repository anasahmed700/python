# object 8
class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometerReading = 500  # OBJECT 9 STEP

    def descriptiveName(self):
        longName = str(self.year) + ' ' + self.make.title() + ' ' + self.model
        return longName

    # Modifying an Attribute’s Value Through a Method
    def updateOdometer(self, mileage):  # from OBJECT 10 STEP
        if mileage >= self.odometerReading:
            self.odometerReading = mileage
        else:
            print('you can\'t roll back the odometer!')


            # Incrementing an Attribute’s Value Through a Method

    def incrementOdometer(self, miles):
        self.odometerReading += miles

    def get_odometer(self):  # from OBJECT 10 STEP
        return self.odometerReading

    def __str__(self):  # FROM OBJECT 12
        return "Make = " + self.make + ", Model =  " + self.model + ", Year = " + str(self.year)


myCar = Car('audi', 'a4', 2016)
name = myCar.descriptiveName()
print(name)

# OBJECT 10
print('\nOBJECTS 10')
print(myCar.get_odometer())

myCar.updateOdometer(2500)
print(myCar.get_odometer())

# Incrementing an Attribute’s Value Through a Method
print('\nINCREMENT IN ODOMETER')
myUsedCar = Car('subaru', 'outback', 2013)
print(myUsedCar.descriptiveName())
myUsedCar.updateOdometer(3000)
myUsedCar.incrementOdometer(100)
print(myUsedCar.get_odometer())

# OBJECT 12
print('\nOBJECT 12')
print(myCar)

# OBJECT 13
print('\nOBJECT 13')


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super(ElectricCar, self).__init__(make, model, year)
        # self.make = make
        # self.model = model
        # self.year = year
        self.batterySize = 70

    # Defining Attributes and Methods for the Child Class
    def charging(self):  # object 15
        print('Electrical car is charging!')

    # Defining Attributes and Methods for the Child Class
    def describe_battery(self):  # object 15
        print('this car has a ' + str(self.batterySize) + '-kWh battery.')


yourCar = ElectricCar('tesla', 's4', 2016)
print(yourCar.descriptiveName())

# OBJECT 14
print('\nOBJECT 14')
yourCar.charging()
yourCar.describe_battery()
