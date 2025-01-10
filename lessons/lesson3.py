# Инкапсуляция


# Открытые
# Защищеные (Protect)  | _
# Приватные (Private)  |

import random

class Hero:


    def __init(self, name, hp, lvl):
        self.name = name
        self.hp = hp
        self.lvl = lvl
        self._luck = random.randint(0, 100)
        self.__crit_dmg = random.randint(0, 100)


    def __heal_hp(self):
        return random.randint(0, 100)

    def rest(self):
        self.hp += self.__heal_hp()

    def defence(self):
        if self._luck >= 20:
            return print(f"{self.name} succesfully defences.")
        else:
            return print(f"{self.name} failed defence.")

    def attack(self):
        if self.__crit_dmg >= 30:
            return print(f"{self.name} critical damage")
        else:
            return print(f"{self.name} regular damage")

kirito = Hero("Kirito", 100, 1)

# print(kirito._luck)
# print(dir(kirito))
print(kirito._Hero__crit_dmg)
