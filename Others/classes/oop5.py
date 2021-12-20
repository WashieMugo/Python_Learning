# Polymophic Objects {let a subclass behave different for some property }
class Feline:
    def speak(self):
        print("Meow")


class Cat(Feline):
    def lick(self):
        print("Licking Paw")


class Lion(Feline):
    def prey(self):
        print("Pounces of Prey")

    def speak(self):   # overides the parent method
        print("Roar")


cat = Cat()
cat.speak()
lion = Lion()
lion.speak()
