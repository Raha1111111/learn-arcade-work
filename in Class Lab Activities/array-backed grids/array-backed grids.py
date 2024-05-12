class Room:
    def __init__(self, description='', north=None, east=None, south=None, west=None):
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west


def main():
    # Create room instances
    balcony1 = Room("You are on the first balcony. There is a door to the north.")
    bedroom = Room("You are in the bedroom. There is a door to the west.")
    kitchen = Room("You are in the kitchen. There are doors to the north and east.")
    dining_hall = Room("You are in the dining hall. There are doors to the west, east, and south.")
    living_room = Room("You are in the living room. There are doors to the north, east.")
    balcony2 = Room("You are on the second balcony. There is a door to the east.")

    # Set room connections
    balcony1.north = bedroom
    kitchen.east = balcony1
    kitchen.west = living_room
    bedroom.west = dining_hall
    living_room.east = kitchen
    living_room.north = balcony2
    dining_hall.west = balcony2
    dining_hall.south = kitchen
    balcony2.east = dining_hall

    # Populate room list
    room_list = [balcony1, kitchen, bedroom, living_room, dining_hall, balcony2]

    # Set current room
    current_room = living_room

    # Print current room description
    print(current_room.description)

    # Game loop
    done = False
    while not done:
        print("\n")
        user_input = input("What do you want to do? ").lower()

        if user_input == "quit":
            print("Quitting the game.")
            done = True
        elif user_input in ["n", "north", "s", "south", "e", "east", "w", "west"]:
            direction = ""
            if user_input == "n":
                direction = "north"
            elif user_input == "s":
                direction = "south"
            elif user_input == "e":
                direction = "east"
            elif user_input == "w":
                direction = "west"

            next_room = getattr(current_room, direction)
            if next_room is None:
                print("You can't go that way.")
            else:
                current_room = next_room
                print(current_room.description)
        else:
            print("Sorry, I don't understand that command.")


if name == "__main__":
    main()

