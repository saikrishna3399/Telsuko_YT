class Computer:

    def __init__(self):
        self.name = "Krishna"
        self.age = 28

    def update(self):
        self.age = 30


c1 = Computer()
c2 = Computer()

c1.name = "Radha"
c1.age = 24

print(c1.name)
print(c2.name)