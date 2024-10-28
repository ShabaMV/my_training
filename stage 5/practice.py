class Human():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.say_info()

    def __del__(self):
        print(f"{self.name} ушел")

    def __len__(self):
        return self.age

    def __lt__(self, other):
        return self.age < other.age

    def __gt__(self, other):
        return self.age > other.age

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    def __bool__(self):
        return bool(self.age)

    def say_info(self):
        print(f"Привет, меня зовут {self.name}! Мне {self.age}")

    def birthday(self):
        self.age += 1
        print(f"У меня день рождения, мне теперь {self.age}")

den = Human("Денис", 22)
max = Human("Максим", 18)
print(max < den)
print(max > den)
print(max == den)
if den:
    den.say_info()
max.birthday()
