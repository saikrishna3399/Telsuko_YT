# Class - Design or Blue Print
# Object - Instance
# Why Use Classes?
# Classes are used to model real-world things or concepts and to bundle data and functionality together.
# This approach helps in organizing and managing complex programs more efficiently.

# Summary
# Class: A blueprint for creating objects.
# Object: An instance of a class.
# Attributes: Data stored in an object.
# Methods: Functions that operate on the object's data.

class Computer:

    def __init__(self, cpu_comp, ram_comp):  # init to initialise variables
        # self = comp1, cpu = M3, ram = 32
        self.cpu = cpu_comp
        self.ram = ram_comp

    def config(self):  # Method - Behaviour (Same as function, but we call it Method in Class )
        print("Config is ", self.cpu, self.ram)


comp1 = Computer('M3', 32) # Defining Variables or Config Data passing Values to Init
comp2 = Computer('i9', 16)

print(type(comp1))

# Computer.config(comp1)
# Computer.config(comp2)

comp1.config() # running the behaviour here
comp2.config()
