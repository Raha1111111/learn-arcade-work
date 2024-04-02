
room_list = [
    {"name": "kitchen", "description": "You are in the kitchen. There is a door to the north.", "north": 1,
     "east": None, "south": None, "west": None},
    {"name": "bedroom", "description": "You are in the bedroom. There is a door to the south and west.", "north": None,
     "east": None, "south": 0, "west": 2},
    {"name": "garden", "description": "You are in the garden. There is a door to the east.", "north": None, "east": 1,
     "south": None, "west": None}
]

# Start the player in the kitchen
current_room = 0

# Main game loop
while True:
    # Print the current room's description
    print(room_list[current_room]["description"])

    # Get user input
    command = input(">").lower()

    # Handle user input
    if command == "quit":
        print("Thanks for playing!")
        break
    elif command == "north":
        next_room = room_list[current_room]["north"]
        if next_room is None:
            print("You can't go that way.")
        else:
            current_room = next_room
    elif command == "east":
        next_room = room_list[current_room]["east"]
        if next_room is None:
            print("You can't go that way.")
        else:
            current_room = next_room
    elif command == "south":
        next_room = room_list[current_room]["south"]
        if next_room is None:
            print("You can't go that way.")
        else:
            current_room = next_room
    elif command == "west":
        next_room = room_list[current_room]["west"]
        if next_room is None:
            print("You can't go that way.")
        else:
            current_room = next_room
    else:
        print("I'm sorry, I don't understand that command.")

    print()

