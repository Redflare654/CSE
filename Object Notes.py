class Laptop(object):
    def __init__(self, screen_resolution, extra_space, colour):
        # Things that a laptop has.
        # Everything in this list should be relevant to the program
        self.processor = "Intel i5"
        self.screen_resolution = screen_resolution
        self.battery_left = 100
        self.spaceleft = extra_space
        self.color = colour
        self.os = "Window"

    def charge(self, time):
        # computer is already charged
        if self.battery_left >= 100:
            print("the computer is already charged")
            return

        self.battery_left += time  # This adds to the battery life
        # computer is mostly charged
        if self.battery_left > 100:
            print("The computer quickly charges")
            self.battery_left = 100
        # computer is not charged at all
        else:
            print("The computer is now at %d%%" % self.battery_left)
my_computer = Laptop("1920x1080", 10000, "Black")
your_computer = Laptop("10x10", 0, "Orange")
wiebe_computer = Laptop("900000000000000x900000000", 99999999999999, "awesome")