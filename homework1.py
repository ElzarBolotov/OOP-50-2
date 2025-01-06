class Hero:
    def __init__(self, name, lvl, HP):
        self.name = name
        self.lvl = lvl
        self.HP = HP

    def introduce(self):
        print(f"Привет, меня зовут {self.name}, мой lvl {self.lvl}, мое HP {self.HP}")

    def is_adult(self):
        return self.lvl >= 10

    def __str__(self):
        return f"Имя: {self.name}, lvl: {self.lvl}, HP: {self.HP}"

hero1 = Hero(name="Эльзар", lvl=999, HP=100)
hero2 = Hero(name="Тилек", lvl=1, HP=150)
hero3 = Hero(name="Акылай", lvl=10, HP=200)

hero1.introduce()
print("Является взрослым:", hero1.is_adult())
print(hero1)

hero2.introduce()
print("Является взрослым:", hero2.is_adult())
print(hero2)

hero3.introduce()
print("Является взрослым:", hero3.is_adult())
print(hero3)
