
class Room:
    def __init__(self, description, north=None, east=None, south=None, west=None):
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west

def main():
    room_list = []

    # Create rooms based on the sketch
    room_list.append(Room("You are in the Living Room. There is a passage to the east to the Kitchen, and south to the Balcony.", None, 1, 3, None))  # 0 Living Room
    room_list.append(Room("You are in the Kitchen. Exits lead west to the Living Room and east to the Restroom.", None, 2, None, 0))  # 1 Kitchen
    room_list.append(Room("You are in the Restroom. Exit leads west to the Kitchen.", None, None, None, 1))  # 2 Restroom
    room_list.append(Room("You are on the Balcony. Exits lead north to the Living Room and east to the Dining Hall.", 0, 4, None, None))  # 3 Balcony
    room_list.append(Room("You are in the Dining Hall. Exits lead west to the Balcony and east to the Bedroom.", None, 5, None, 3))  # 4 Dining Hall
    room_list.append(Room("You are in the Bedroom. Exit leads west to the Dining Hall.", None, None, None, 4))  # 5 Bedroom

    current_room = 0
    done = False

    while not done:
        print("\n" + room_list[current_room].description)
        direction = input("What do you want to do? (n/e/s/w/quit): ")

        if direction.lower() in ["n", "north"]:
            next_room = room_list[current_room].north
            if next_room is None:
                print("You can't go that way.")
            else:
                current_room = next_room
        elif direction.lower() in ["e", "east"]:
            next_room = room_list[current_room].east
            if next_room is None:
                print("You can't go that way.")
            else:
                current_room = next_room
        elif direction.lower() in ["s", "south"]:
            next_room = room_list[current_room].south
            if next_room is None:
                print("You can't go that way.")
            else:
                current_room = next_room
        elif direction.lower() in ["w", "west"]:
            next_room = room_list[current_room].west
            if next_room is None:
                print("You can't go that way.")
            else:
                current_room = next_room
        elif direction.lower() in ["quit", "q"]:
            done = True
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()
