world_map = {
    'R19A': {
        'NAME': "Mr. Wiebe's room",
        'DESCRIPTION': "This is the room that you are in.",
        'PATHS': {
            'NORTH': "PARKING_LOT",
            'WEST': "W_BUILDING"
        }
    },
    'PARKING_LOT': {
        'NAME': "A Parking Lot",
        'DESCRIPTION': "There are a few cars parked here.",
        'PATHS': {
            'SOUTH': 'R19A',
            'WEST': 'FAMILY_DOLLAR'
        }
    },
    'FAMILY_DOLLAR': {
        'NAME': "family dollar store",
        'DESCRIPTION': "There a store named family dollar the store looks abandoned",
        'PATHS': {
            'EAST': 'PARKING_LOT',
            'SOUTH': 'EMPTY_HOUSE'
        }
    },
    'W_BUILDING': {
        'NAME': "The w building",
        'DESCRIPTION': "there a building that shape of a w but it appear to be boarded up there no where else to go",
        'PATHS': {
            'EAST': 'R19A'
        }
    },
    'EMPTY_HOUSE': {
      'NAME': "Le empty house",
      'DESCRIPTION': "you see an empty house the windows are nailed shut so is the door ",
      'PATHS': {
          'NORTH': 'FAMILY_DOLLAR',
          'SOUTH': 'FOREST'
        }
    },
    'FOREST': {
      'NAME': "Le forest where birds and bees are",
      'DESCRIPTION': "you see the forset if you go in there you cant go back have fun exploring the forest",
      'PATHS': {
          'SOUTH': 'RIVER',
          'EAST': 'MOUNTAIN'
      }
    },
    'MOUNTAIN': {
      'NAME': "Mount Hood",
      'DESCRIPTION': "You look around and you see a bootiful veiw of other mountains",
      'PATHS': {
            'WEST': 'FOREST',
            'NORTH': 'HOLE',
      }
    },
    'HOLE': {
      'NAME': "deep hole",
      'DESCRIPTION': "you look around and you see a big deep hole and you dont know where it goes too",
      'PATHS': {
          'DOWN': 'IN_THE_HOLE',
          'WEST': 'CAVE'
      }
    },
    'RIVER': {
      'NAME': "Ravi River",
      'DESCRIPTION': "you see water and when you look around you realize that you arrive at a"
                     " river and the surrounding are beautiful",
      'PATHS': {
          'NORTH': 'FOREST'
      }
    },
    'CAVE': {
      'NAME': "scary cave",
      'DESCRIPTION': "you enter a cave it every dark and creepy but it a dead end",
      'PATHS': {
          'EAST': 'HOLE'
      }
    },
    'IN_THE_HOLE': {
       'NAME': "Underground",
       'DESCRIPTION': " you fell 50ft from the sky and you are alive somehow you look"
                      " around and it seem you landed on dead flowers and everything around you is gray",
       'PATHS': {
           'NORTH': 'OLD_PATHWAY'
       }
    },
    'OLD_PATHWAY': {
        'NAME': "Very old pathway",
        'DESCRIPTION': "you look around again and you see a door frame that led a path you look "
    }
}

# Other Variables
directions = ["NORTH", "SOUTH", "EAST", "WEST", "UP", "DOWN"]
current_node = world_map["R19A"]  # This is your current location
playing = True

# Controller
while playing:
    print(current_node['NAME'])
    print(current_node['DESCRIPTION'])

    command = input(">_")
    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command in directions:
        try:
            room_name = current_node["PATHS"][command]
            current_node = world_map[room_name]
        except KeyError:
            print("I can't go that way.")
    else:
        print("Command not recognized.")
