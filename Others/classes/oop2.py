# Inheritance:
# Ex 1
class Parent:
    def __init__(self):
        self.eyes = "green"


class Child(Parent):
    def __init__(self):
        super().__init__()
        self.age = 7


child = Child()
print(child.eyes)
print(child.age)

# EX 2


class Greetings:
    def greet(self):
        print("Hi")


class Person(Greetings):
    name = "Washington"


p = Person()
p.greet()

# EX 3


class Car:
    def start_car(self):
        print("starting car...")


class Hybrid(Car):
    def charge(self):
        print("Using fuel to charge")


prius = Hybrid()
prius.start_car()
prius.charge()
