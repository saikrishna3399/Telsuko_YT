class Car:
    def __init__(self, segment, engine_type, brand):
        self.segment = segment
        self.engine_type = engine_type
        self.brand = brand

    def config(self):
        print("Your Car is ", self.brand, self.engine_type, "Engine", self.segment)


car1 = Car('Suv', 'Deisel', 'Tata')
car2 = Car('Coupe Suv', 'Petrol', 'Ferrarri')

print(car1.config())  # Very Interesting mistake I made :p
car2.config()
