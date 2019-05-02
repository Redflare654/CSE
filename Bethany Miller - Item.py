class Item(object):
    def __init__(self, name):
        self.name = name


class Food(object):
    def __init__(self, name):
        super(Food, self).__init__(name)
        self.energy = True


class Flashlight(Item):
    def __init__(self, name):
        super(Flashlight, self).__init__(name)
        self.power = True

    def power_on(self):
        self.power = True
        print("you turn on the flashlight now you are blind for a couple of seconds")


class Chocolate(Item):
    def __init__(self, name):
        super(Chocolate, self).__init__(name)
        self.gives_energy = 5

    def gives_energy(self):
        self.gives_energy = 5
        print("You eat de chocolate and it gives you energy and you are not hungry no more. yay!!!! you wont die now")


class Weapon(Item):
    def __init__(self, name, damage):
        super(Weapon, self).__init__(name)
        self.damage = damage


class Armor(Item):
    def __init__(self, name, armor_amt):
        super(Armor, self).__init__(name)
        self.armor_amt = armor_amt


class Phone(Item):
    def __init__(self, name):
        super(Phone, self).__init__(name)
        self.power = True
        self.battery_left = 100


class Water(Food):
    def __init__(self, name):
        super(Water, self).__init__(name)
        self.heat = -10


class Rope(Item):
    def __init__(self, name):
        super(Rope, self).__init__(name)
        self.strength = 100


class Headphone(Item):
    def __init__(self, name):
        super(Headphone, self).__init__(name)
        self.used = 57
        self.working = True


class Backpack(Item):
    def __init__(self, name):
        super(Backpack, self).__init__(name)
        self.space = 35
        self.water_holder = 2


class Jacket(Item):
    def __init__(self, name):
        super(Jacket, self).__init__(name)
        self.give_warmth = True

    def give_warmth(self):
        self.give_warmth = 54
        print("you put on a jacket you wont freeze now")


class Gloves(Item):
    def __init__(self, name):
        super(Gloves, self).__init__(name)
        self.protection = True


class Ball(Item):
    def __init__(self, name):
        super(Ball, self).__init__(name)
        self.bounce = 100


class Watch(Item):
    def __init__(self, name):
        super(Watch, self).__init__(name)
        self.battery = 150


class Necklace(Item):
    def __init__(self, name):
        super(Necklace, self).__init__(name)
        self.beauty = 75
