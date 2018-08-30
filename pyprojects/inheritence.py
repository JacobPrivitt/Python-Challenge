class AutoMobile:
    model_year = "2019"

    def start(self):
        print("Auto is starting.")

    def turn_off(self):
        print("Vehichle is off.")

class Truck(AutoMobile):

    def __init__(self, year =None):
        if year is None:
            self.year = 2018
        else:
            self.year = year

    def __str__(self):
        return("2019 truck sold by ford.")

    def truck_year(self):
        print("This truck was built in: " + str(self.year))

    def dumpload(self, dump =None):
        if dump is None:
            print("There is nothing to dump!")
        else:
            print("Truck is dumping " + str(dump))

    

my_car = Truck("2020")
my_car.truck_year()
my_car.dumpload("10")


