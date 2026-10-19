
class Character:
    def __init__(self, name, power, health, coins):
        self.name = name
        self.power = power
        self.health = health
        self.coins = coins
        self.level = 1

    def show_info(self):
        print(self.name, "| Level:", self.level, "| Power:", self.power, "| Health:", self.health, "| Coins:", self.coins)

    def is_alive(self):
        return self.health > 0

    def attack(self, other):
        other.health = other.health - self.power
        print(self.name, "attacked", other.name, ".")
        print(other.name, "'s health:", other.health)

    def earn_coins(self, amount):
        self.coins = self.coins + amount

    def buy_potion(self):
        if self.coins >= 20:
            self.coins = self.coins - 20
            self.health = self.health + 30
        else:
            print("Dont have enough coins")

    def level_up(self):
        self.level = self.level + 1
        self.power = self.power + 5
        print(self.name, "reached level", self.level, ". New power:", self.power)


character1 = Character("Arya", 10, 100, 50)
character2 = Character("Bran", 8, 100, 30)

character1.attack(character2)
character2.attack(character1)
character1.attack(character2)

character1.buy_potion()
character2.level_up()

print()

print("Character 1:")
character1.show_info()

print()

print("Character 2:")
character2.show_info()
