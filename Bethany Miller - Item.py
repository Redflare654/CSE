class Item(object):
    def __init__(self, name):
        self.name = name


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
