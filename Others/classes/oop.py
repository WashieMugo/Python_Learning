class Rectangle:
    base = 3
    height = 4

    def getArea(self):
        return self.base*self.height


rect = Rectangle()
area = rect.getArea()
print(area)


class Person:
    name = "Sam"

    def greet(self, name):
        print(f"Hi {name}")


p = Person()
p.greet("Washington")
