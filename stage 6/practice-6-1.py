class Human:
    def __init__(self, name, group):
        self.name = name
        super().__init__(group)

    def info(self):
        print(f"Привет, мну звт {self.name}")

class StudentGroup:
    def __init__(self, group):
        self.group = group
    def about(self):
        print(f"{self.name} учится в группе {self.group}")

class Student(Human, StudentGroup):
    def __init__(self,name, place, group):
        super().__init__(name, group)
        self.place = place
        super().info()

# human = Human('Михаил')
# print(human.name)
student = Student('Макс', 'UrbanUnivercity',202)
student.about()
# print(Student.mro())