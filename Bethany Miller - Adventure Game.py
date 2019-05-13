class Room(object):
    def __init__(self, description="insert description", name=None, north=None, south=None, east=None, west=None,
                 up=None, down=None, item=None):
        if item is None:
            item = []
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.up = up
        self.down = down
        self.description = description
        self.item = item


class Item(object):
    def __init__(self, name):
        self.name = name


class Character(object):
    def __init__(self, name, health, weapon, armor):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.armor = armor

    def take_damage(self, damage):
        if damage < self.armor.armor_amt:
            print("No damage is done because of some FABULOUS armor!")
        else:
            self.health -= damage - self.armor.armor_amt
            if self.health < 0:
                self.health = 0
                print("%s has fallen" % self.name)
        print("%s has %d health left" % (self.name, self.health))

    def attack(self, target):
        print("%s attacks %s for %d damage" %
              (self.name, target.name, self.weapon.damage))
        target.take_damage(self.weapon.damage)


class Flashlight(Item):
    def __init__(self, name):
        super(Flashlight, self).__init__(name)
        self.power = True

    def power_on(self):
        self.power = True
        print("you turn on the flashlight now you are blind for a couple of seconds")


class Food(Item):
    def __init__(self, name):
        super(Food, self).__init__(name)
        self.gives_energy = True

    def gives_energy(self):
        self.gives_energy = True
        print(
            "You eat de %s and it gives you energy and you are not hungry no more. yay!!!! you wont die now" %
            self.name)


class Chocolate(Food):
    def __init__(self, name):
        super(Chocolate, self).__init__(name)
        self.gives_energy = 5


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

    def space(self):
        if item in player.inventory:
            self.space = -1


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


class Player(object):
    def __init__(self, starting_location):
        self.heath = 100
        self.inventory = []
        self.current_location = starting_location

    def move(self, new_location):
        """This method moves player to a new location

        :param new_location: The room object that we move to
        """
        self.current_location = new_location

    def find_room(self, direction):
        """This method

        :param direction:
        :return:
        """
        return getattr(self.current_location, direction)


chocolate = Chocolate("Chocolate Bar")
water = Water("Water bottle")
flashlight = Flashlight("Flashlight")
phone = Phone("Cellphone")
rope = Rope("The rope it can do many thing")


# Options 1 - Use the variables , but fix later
R19A = Room("this is a classroom", "Mr.Wiebe's room")
parking = Room("There are a few cars parked here.", "The parking lot")
family_dollar = Room("There a store named family dollar the store looks abandoned", "OLD FAMILY DOLLARS")
empty_house = Room("you see an empty house the windows are nailed shut so is the door",  "le empty house")
forest = Room("you see the forest if you go in there you cant go back have fun exploring the forest",  "Forest")
mountain = Room("You look around and you see a beautiful view of other mountains",  "Mount hood")
hole = Room("you look around and you see a big deep hole and you don't know where it goes too",  "Hole")
in_the_hole = Room("you fell very deep and lived yay!",  "Underground")
old_pathway = Room("you look around again and you see a door frame that led a path",  "old pathway")
old_house = Room("you wonder who use to live here a human or something else", "very old house")
inside_house = Room("around you see a picture of a family of goats and one human and as you look at the picture you "
                    "question life as you question life you see a stair case that leads down and you wonder "
                    "where that lead to ", "inside the house")
snowing_area = Room("you went down the stairs you see a door open as you see dust everywhere and you still question "
                    "life while you do that you when through the door once "
                    "you step on the other side you heard a crunch "
                    "sound you look down you see snow you thought how can snow be "
                    "here you also wonder what else can be here",
                    "snowing area")
snowed_house = Room("you walked around you see a snowed up house with 2 mail box and you wonder why there only one"
                    "them stuffed with paper and you also notice they both have names on them on is sans the other is"
                    "papyrus", "Sans and Papyrus house")
waterfall = Room("you looked around more and it looked like you've walked in to a town of snow but you kept walking "
                 "and you see water everywhere so you called this area waterfall and it looked beautiful", "Waterfall")
echo_flower = Room("when you pass water fall you see blue flowers everywhere and there also glowing you said something"
                   "the flowers repeated what you said over and over again", "Echo")
Hotland = Room("as you walked through you started to feel hot when you looked around you see lava everywhere and then"
               "you see a building you walked up to it and the the door is open so you went in", "Hotland")
The_lab = Room("when you walked in the room it looked like an old lab and it was dark too you walked around the next"
               "thing you notice there was a water fountain and a hot dog stand and you kept walking", "the lab")
New_home = Room("after you got out the lab you seen a sign called new home but it looked very old you called old home",
                "Old Home")
Judgement_hall = Room("while you walk you've walked into a hall and there was a pile of dust and holes in the walls "
                      "everywhere and one have a blue bone sticking out", "Judgement Hall")
The_cave = Room("as you walked by you seen a cave which label the barrier and this where it all ends", "The Cave")
Outside = Room("once you were out of the cave you seen a beautiful view of the forest and it was quite relaxing",
               "Outside")


R19A.item = [water]
family_dollar.item = [rope, water]
empty_house.item = [phone, chocolate]
mountain.item = [flashlight]


R19A.north = parking
parking.south = R19A
parking.west = family_dollar
family_dollar.south = empty_house
empty_house.south = forest
forest.east = mountain
mountain.north = hole
hole.down = in_the_hole
in_the_hole.north = old_pathway
old_pathway.west = old_house
old_house.west = inside_house
inside_house.down = snowing_area
snowing_area.north = snowed_house
snowed_house.north = waterfall
waterfall.west = echo_flower
echo_flower.north = Hotland
Hotland.up = The_lab
The_lab.north = New_home
New_home.west = Judgement_hall
Judgement_hall.up = The_cave
The_cave.up = Outside


player = Player(R19A)

directions = ['north', 'south', 'east', 'west', 'up', 'down']
short_directions = ['n', 's', 'e', 'w', 'up', 'd']
playing = True

# Controller
while playing:
    print(player.current_location.name)
    print(player.current_location.description)
    if len(player.current_location.item) > 0:
        for item in player.current_location.item:
            print("There is a %s here." % item.name)

    command = input(">_")

    if command in short_directions:
        pos = short_directions.index(command)
        command = directions[pos]

    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command in directions:
        try:
            next_room = player.find_room(command)
            if next_room is None:
                raise KeyError
            player.move(next_room)
        except KeyError:
            print("I can't go that way.")
    elif "pick up " in command:
        item_name = command[8:]

        found_item = None
        for item in player.current_location.item:
            if item_name == item_name:
                found_item = item

        if found_item is None:
            print("I don't see one")
        else:
            player.inventory.append(found_item)
            player.current_location.item.remove(found_item)
            print("you picked up le %s" % item_name)
    else:
        print("Command not recognized.")
