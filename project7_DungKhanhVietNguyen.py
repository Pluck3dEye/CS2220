# Dung K.V. Nguyen (1607859)

# Problem #11 page 133
# The program is inspired by RPG games. Superclass is Character, subclasses are Dragon and DragonSlayer
import random


class Character:
    def __init__(self, name, health, strength):  # Basic properties
        self.name = name
        self.__health = health
        self.__strength = strength

    def get_health(self):
        return self.__health

    def get_strength(self):
        return self.__strength

    def display_information(self):
        print("Name: " + self.name + " Health: " + str(self.__health) + " Strength: " + str(self.__strength))

    def normal_attack(self, target):
        damage = self.__strength
        print(f"{self.name} attacks {target.name} for {damage} damage!")
        target.take_damage(damage)

    def take_damage(self, damage):
        self.__health -= damage
        if self.__health <= 0:  # When one of character's health reach 0, stop the fight
            self.__health = 0
            print(f"{self.name} died!")


class DragonSlayer(Character):
    def __init__(self, name, health=125, strength=30):
        super().__init__(name, health, strength)

    def last_dance(self, target):
        damage = self.get_strength() * 3
        print(f"{self.name} uses ability \"Last dance\" to {target.name} with {damage} damage!")
        target.take_damage(damage)


class Dragon(Character):
    def __init__(self, name, health=300, strength=20):
        super().__init__(name, health, strength)

    def fire_ball(self, target):
        damage = self.get_strength() + 20
        print(f"{self.name} burns {target.name} for {damage} damage!")
        target.take_damage(damage)


dragon1 = Dragon("Dagahra", 450, 35)
dragon_slayer1 = DragonSlayer("Cadmus", 125, 40)

dragon1.display_information()
dragon_slayer1.display_information()
print()

# Result would be random

while dragon1.get_health() > 0 and dragon_slayer1.get_health() > 0:
    roll = random.randint(1, 6)
    if roll in [1, 4, 6]:
        if roll == 6:
            dragon_slayer1.last_dance(dragon1)
        else:
            dragon_slayer1.normal_attack(dragon1)
    else:
        if roll == 2:
            dragon1.fire_ball(dragon_slayer1)
        else:
            dragon1.normal_attack(dragon_slayer1)
else:
    print()
    dragon1.display_information()
    dragon_slayer1.display_information()
