class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def aboutMe(self):
        print("학생 이름 : %s , 학생 나이 : %d" %(self.name, self.age))

class Student(Person):
    school = "goorm school"

user1 = Student('huewilliams', 17)
user1.aboutMe()