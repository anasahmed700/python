class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometerReading = 500  # OBJECT 9 STEP

    def descriptive_name(self):
        longName = str(self.year) + ' ' + self.make.title() + ' ' + self.model
        return longName

    # Modifying an Attribute’s Value Through a Method
    def update_odometer(self, mileage):  # from OBJECT 10 STEP
        if mileage >= self.odometerReading:
            self.odometerReading = mileage
        else:
            print('you can\'t roll back the odometer!')


            # Incrementing an Attribute’s Value Through a Method

    def increment_odometer(self, miles):
        self.odometerReading += miles

    def get_odometer(self):  # from OBJECT 10 STEP
        return 'This car has '+str(self.odometerReading)+ ' miles on it.'

    def __str__(self):  # FROM OBJECT 12
        return "Make = " + self.make + ", Model =  " + self.model + ", Year = " + str(self.year)


# class Battery():
#     """A simple attempt to model a battery for an electric car."""
#     def __init__(self, battery_size=70):
#         """Initialize the battery's attributes."""
#         self.battery_size = battery_size
#
#     def describe_battery(self):
#         """Print a statement describing the battery size."""
#         print("This car has a " + str(self.battery_size) + "-kWh battery.")
#
#     def get_range(self):
#         if self.battery_size == 70:
#             range = 240
#         elif self.battery_size == 85:
#             range = 270
#         massage = 'this car can go approximately ' + str(range)
#         massage += ' miles on a full charge!'
#         print(massage)
#
# class ElectricCar(Car):
#     def __init__(self,make,model,year):
#         super().__init__(make,model,year)
#         self.battery = Battery()
