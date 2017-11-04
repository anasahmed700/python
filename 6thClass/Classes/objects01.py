# object 15
class Car():

    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.__odometer_reading = 5



    def get_descriptive_name(self):
        long_name = str(self.year)+ ' '+self.make + ' ' + self.model + ' '+ str(self.__odometer_reading)
        return long_name


class Battery():
    """A simple attempt to model a battery for an electric car."""
    def __init__(self, battery_size=70):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        massage = 'this car can go approximately ' + str(range)
        massage += ' miles on a full charge!'
        print(massage)

# b = Battery()
c = Car('audi', 'a4', 2016)


class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery = Battery()

myTesla = ElectricCar('tesla', 's4', 2016)
print(myTesla.get_descriptive_name())

myTesla.battery.describe_battery()

myTesla.battery.get_range()