class Human:
    head = True
    _legs = True
    __arms = True

    def say_hello(self):
        print("Здравствуйте")

    def about(self):
        print(self.head)
        print(self._legs)
        print(self.__arms)

class Student(Human):
    pass
    # def about(self):
    #     print("Я студент")

class Teacher(Human):
    pass

human = Human()
student=Student()

print(dir(Human))
print(student._Human__arms)