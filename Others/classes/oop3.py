# Constructors
class Persons:
    def __init__(self, name, age):
        self.name = name
        self.age = age


sam = Persons("Samuel", 23)
print(f"Welcome {sam.name} i suppose you are {sam.age} Yeas old now.")

# EX 2 ============================


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hi")


class Nurse(Person):
    def __init__(self, name, age):
        super().__init__("Nurse "+name, age)

    def intro(self):
        print("Hi, I'm ", self.name)


person1 = Nurse("Sam", 23)
person2 = Person("Washington", 22)

person1.intro()
person2.greet()
