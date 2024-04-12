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
