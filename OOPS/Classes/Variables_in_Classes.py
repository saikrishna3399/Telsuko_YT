class Car:

    wheels = 4            # Class Variables: Wheels is common to all the objects  and belongs to Class Namespace .

    def __init__(self):   # Variables Inside Init are Instance Variables belongs to Instance Namespaces
        self.mil = 10
        self.com = "BMW"


c1 = Car()
c2 = Car()

c1.mil = 8

Car.wheels = 5

print(c1.com, c1.mil, c1.wheels)
print(c2.com, c2.mil, c2.wheels)
