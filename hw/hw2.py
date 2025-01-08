class Heroes:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
    def action(self):
        print(f'{self.name} готовится к выстрелу.')

    def attack(self):
        print(f'{self.name} стреляет во врага.')

class Archer(Heroes):
    def __init__(self, name, hp, arrows, precision):
        super().__init__(name, hp)
        self.arrows = arrows
        self.precision = precision

    def attack(self):
        if self.arrows > 0:
            self.arrows -= 1
            from random import random
            if random() < self.precision:
                print(f'{self.name} попал!')
            else:
                print(f'{self.name} промазал.')
        else:
            print(f'{self.name} не может атаковать.')

    def rest(self):
        self.arrows += 5
        print(f'{self.name} пополнил стрелы.')

    def status(self):
        return f"Имя: {self.name}, Здоровье: {self.hp}, Стрелы: {self.arrows}, Точность: {self.precision}"

archer = Archer("Эльзар", 99, 5, 0.9)

print(archer.status())
archer.attack()
archer.rest()
print(archer.status())

