class Animal:
    def make_sound(self):
        print("sound")

class Flyable(Animal):

    def fly(self):
        return print("I'm flying")


class Swinmmanble(Animal):

    def swim(self):
        return print("I'm swim")

class Voron(Flyable):
    pass

class Duck(Flyable, Swinmmanble):
    pass

donald_duck = Duck()

donald_duck.fly()
donald_duck.swim()