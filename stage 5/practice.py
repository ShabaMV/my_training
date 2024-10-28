class Human():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.say_info()

    def __del__(self):
        print(f"{self.name} ушел")

    def __len__(self):
        return self.age
    
    def say_info(self):
        print(f"Привет, меня зовут {self.name}! Мне {self.age}")

    def birthday(self):
        self.age += 1
        print(f"У меня день рождения, мне теперь {self.age}")

den = Human("Денис", 22)
max = Human("Максим", 18)
print(len(den))
max.birthday()
