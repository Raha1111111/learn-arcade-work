class Cat:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def meow(self):
        print(self.name + " says: Meow!")


my_cat = Cat("RAHA", "Black", 3.5)
my_cat.meow()


class Monster:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def decrease_health(self, amount):
        self.health -= amount
        if self.health <= 0:
            print(self.name + " died!")


my_monster = Monster("Ajina", 80)
my_monster.decrease_health(70)


class Star:
    def __init__(self, name):
        self.get_name = name
        print("A star is born! It's name is" + name)

    def get_name(self):
        print("A star is born! It's name is" + self.get_name)


star1 = Star(" Neptune")
star2 = Star(" Luna")


class Monster:
    def __init__(self, name, health):
        self.name = name
        self.health = health


monster1 = Monster("O'lmas kashak", 100)
monster2 = Monster("King_monster", 75)

print(monster1.name, "has health:", monster1.health)
print(monster2.name, "has health:", monster2.health)
