class Person:
    def __init__(self, name_person, age_person):
        self.name = name_person # attributes Definition
        self.age = age_person

    def Intro(self):
        print("Hi My name is :" , self.name, "I am :", self.age, " Years Old")


person1 = Person('Krishna', '28')
person2 = Person('Radha', '24')

person2.Intro()
person1.Intro()
