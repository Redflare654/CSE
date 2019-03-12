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
