import random

class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed):
        self._cords = [0, 0, 0]
        self.speed = speed

    def move(self, dx, dy, dz):
        self._cords[0] = dx * self.speed
        self._cords[1] = dy * self.speed
        if dz < 0:
            print("It's too deep, i can't dive :(")
        else:
            self._cords[2] = dz * self.speed

    def get_cords(self):
        print(f"X:{self._cords[0]}, Y:{self._cords[1]}, Z:{self._cords[2]}")

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")

    def speak(self):
        print(self.sound)

class Bird(Animal):
    def __init__(self, speed):
        super().__init__(speed)
        self.beak = True

    def lay_eggs(self):
        number_of_egg = random.randint(1, 4)
        print(f"Here are(is) {number_of_egg} eggs for you")


class AquaticAnimal(Animal):

    def __init__(self, speed):
        super().__init__(speed)
        self._DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        self._cords[2] = self._cords[2] - (abs(dz) / 2) * self.speed

class PoisonousAnimal(Animal):
    def __init__(self, speed):
        super().__init__(speed)
        self._DEGREE_OF_DANGER = 8

class Duckbill(Bird,PoisonousAnimal,AquaticAnimal):
    # sound = "Click-click-click"
    def __init__(self, speed):
        super().__init__(speed)
        self.sound = "Click-click-click"


db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()

db.lay_eggs()

# Относительно этого скрипта возник вопрос. Вероятно, имеющий отношение к версии PY. Ибо, изначально
# не описывая super().__init__() ни в одном из классов получил тот же результат. Мне показалось, что
# PY самостоятельно определил верно последовательность инитов в зависимости от уровня вложенности
# дочернего класса? Это является допущением или ошибкой?