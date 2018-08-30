#Jaocb Privitt

class Car():
    ''' A simple class that discribles a car '''

    def __init__ (self, model, cost):
        ''' Initalizing the object '''
        self.model = model
        self.cost = cost


    def start(self):
        ''' Starts the car '''
        print(self.model.title() + " is now starting.")


# Class vs Object

myCar = Car("audi", "$90K")
myCar.start()
