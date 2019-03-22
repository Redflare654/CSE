"""
class Vehicle(object):
    def __init__(self, name):
        self.name = name


class Car(Vehicle):
    def __init__(self, name):
        super(Car, self).__init__(name)
        self.engine_status = False
        self.fuel = 100

    def start_engine(self):
        self.engine_status = True
        print("you turn the key an the engine starts")

    def move_forward(self):
        self.fuel -= 1
        print("you move forward")

    def turn_left(self):
        self.fuel -= 1
        print("HE'S MAKING A LEFT TURN")

    def turn_off(self):
        self.engine_status = False
        print("You turn the engine off")


class Viper(Car):
    def __init__(self):
        super(Viper, self).__init__("Viper")


class Tesla(Car):
    def __init__(self):
        super(Tesla, self).__init__("Tesla")

    def start_engine(self):
        self.engine_status = True
        print("You push the button and the engine starts")


bethany_car = Viper()
bethany_car.start_engine()
bethany_car.move_forward()
bethany_car.turn_left()
bethany_car.move_forward()
bethany_car.turn_off()
print()

brisa_car = Tesla()
brisa_car.start_engine()
brisa_car.move_forward()
"""

class Item(object):
    def __init__(self, name):
        self.name = name


class Weapon(Item):
    def __init__(self, name, damage):
        super(Weapon, self).__init__(name)
        self.damage = damage


class Armor(Item):
    def __init__(self, name, armor_amt):
        super(Armor, self).__init__(name)
        self.armor_amt = armor_amt


class Character(object):
    def __init__(self, name, health, weapon,armor):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.armor = armor

    def take_damage(self, damage):
        if damage < self.armor.armor_amt:
            print("welp lucky you, you took no damage cause you have something called an armor on you")
        else:
             self.health -= damage - self.armor.armor_amt
             if self.health < 0:
                self.health = 0
                print("%s has fallen" % self.name)
        print("% has %d health left" % (self.name, self.health))

    def attack(self, target):
        print("%s attacks %s for %d damage" % (self.name, target.name, self.weapon.damage))


# Item
sword = Weapon("Sword", 10)
canoe = Weapon("canoe", 84)
wiebe_armor = Armor("Wiebe Armor", 75)

