# class Human():
#
#     head = True
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.say_info()
#
#     def __del__(self):
#         print(f"{self.name} ушел")
#
#     def __len__(self):
#         return self.age
#
#     def __lt__(self, other):
#         return self.age < other.age
#
#     def __gt__(self, other):
#         return self.age > other.age
#
#     def __eq__(self, other):
#         return self.name == other.name and self.age == other.age
#
#     def __bool__(self):
#         return bool(self.age)
#
#     def say_info(self):
#         print(f"Привет, меня зовут {self.name}! Мне {self.age}")
#
#     def birthday(self):
#         self.age += 1
#         print(f"У меня день рождения, мне теперь {self.age}")
#
# den = Human("Денис", 22)
# max = Human("Максим", 18)
# print(max < den)
# print(max > den)
# print(max == den)
# if den:
#     den.say_info()
# max.birthday()
# print(Human.head)
# print(Human.__dict__)

class User:
    __instance = None
    def __new__(cls, *args, **kwargs):
        print('Я в new')
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance
    def __init__(self, *args, **kwargs):
        print('Я в ините')
        self.args = args
        self.kwargs = kwargs
        for key,val in kwargs.items():
            setattr(self, key, val)

other = [1, 2, 3]
user = {'name': 'Den', 'age': 25}
user1 = User(*other, **user)
print(user1.args)
print(user1.kwargs)
print(user1.name)
print(user1.age)