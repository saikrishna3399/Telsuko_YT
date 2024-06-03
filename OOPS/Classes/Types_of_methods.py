class Student:
    school = 'Takshila'

    def __init__(self, m1_marks, m2_marks, m3_marks):
        self.m1 = m1_marks
        self.m2 = m2_marks
        self.m3 = m3_marks

    def avg(self):
        return (self.m1 + self.m2 + self.m3) / 3

    def get_m1(self):
        return self.m1

    def set_m1(self, value):
        self.m1 = value

    @classmethod
    def get_school(cls):
        return cls.school

    @staticmethod
    def info():
        print("This is a Student Class!!!")


s1 = Student(36, 24, 36)
s2 = Student(69, 42, 96)

print(s1.avg())
print(s2.avg())

print(Student.get_school())

Student.info()