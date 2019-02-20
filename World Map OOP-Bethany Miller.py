class Room(object):
    def __init__(self, name, north=None, south=None, east=None, west=None, up=None, down=None):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.up = up
        self.down = down


# Options 1 - Use the variables , but fix later
R19A = Room("Mr.wiebe's room ")
parking = Room("the parking lot", None, "R19A")

R19A.north = parking

#  Option 2 - Use strings, but more diffcult controller
R19A = Room("Mr.Wiebe's Room", 'parking')
parking = Room("The parking lot", None, "R19A")