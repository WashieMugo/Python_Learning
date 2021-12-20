# Abstracting obejcts
class Car:
    def __init__(self):
        self.on = False

    def injectFuel(self):
        print("Spraying Fuel..")

    def igniteFuel(self):
        print("Igniting Fuel")

    def startUp(self):
        self.on = True
        count = 0
        while self.on and count <= 10:
            self.injectFuel()
            self.igniteFuel()
            count += 1


myCar = Car()
myCar.startUp() # the core method. no need to know what the oher methods do
