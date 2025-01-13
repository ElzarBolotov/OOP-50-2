import random
from abc import ABC, abstractmethod


class Hero(ABC):
    def __init__(self, name, health, attack_power, defense_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.defense_power = defense_power
        self.__random_int = random.randint(1, 3)

    def attack(self):
        print(f"{self.name} атакует {self.attack_power}!")

    def protection(self):
        print(f"{self.name} защищается {self.defense_power}!")

    def rest(self):
        self.health += 10
        print(f"{self.name} отдыхает {self.health}.")

    def get_random_int(self):
        return self.__random_int

    @abstractmethod
    def unique_attack(self):
        pass

    @abstractmethod
    def unique_scream(self):
        pass

    @abstractmethod
    def action(self):
        pass


class Jester(Hero):
    def unique_attack(self):
        print(f"{self.name} выполняет хаотичную атаку!")

    def unique_scream(self):
        print(f"{self.name} смеётся!'")

    def action(self):
        random_action = self.get_random_int()
        if random_action == 1:
            self.attack()
        elif random_action == 2:
            self.protection()
        elif random_action == 3:
            self.rest()

jester = Jester(name="Остроумный шут", health=100, attack_power=15, defense_power=10)
jester.unique_attack()
jester.unique_scream()
jester.action()
