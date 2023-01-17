## Single Inheritance

class Car:

    def __init__(self, body, engin, tyre):
        self.body1 = body
        self.engin1 = engin
        self.tyre1 = tyre

    def milage(self):
        return ("Good Milage")


class Tata(Car):
    pass


c = Car("solid", "v4", "MRF")
print(c)
print(c.tyre1)
t = Tata("metal", "v6", "Radial")
print(t)
print(t.milage())
print(t.body1)
