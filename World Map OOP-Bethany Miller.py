class Room(object):
    def __init__(self, name, north=None, south=None, east=None, west=None, up=None, down=None, description=None):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.up = up
        self.down = down
        self.description = description


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


# Options 1 - Use the variables , but fix later
R19A = Room("Mr.wiebe's room ")
parking = Room("the parking lot", None, "R19A")
family_dollar = Room("Family dollar", None, "parking")
empty_house = Room("le empty house", None, "family_dollar")
forest = Room("Forest", None, "empty_house")
mountain = Room("Mountain", None, "forest")


R19A.north = parking
parking.south = R19A
parking.west = family_dollar
family_dollar.south = empty_house
empty_house.south = forest
forest.east = mountain
mountain.south =


player = Player(R19A)

directions = ['north', 'south', 'east', 'west', 'up', 'down']
playing = True

# Controller
while playing:
    print(player.current_location.name)
    print(player.current_location.description)

    command = input(">_")
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
    else:
        print("Command not recognized.")