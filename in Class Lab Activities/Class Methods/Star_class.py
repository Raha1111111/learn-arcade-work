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
