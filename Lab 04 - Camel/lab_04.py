import random


def main():
  done = False
  distance_traveled = 0
  thirst = 0
  camel_tiredness = 0
  distance_natives = -20
  drinks_in_canteen = 3

  while not done:
    random_num = random.randint(7, 14)
    random_move = random.randint(10, 20)
    random_go_ahead = random.randint(5, 12)
    random_camel_tiredness = random.randint(1, 3)
    random_oasis = random.randint(1, 20)

    print(
        "\nA. Take a sip from your water flask.\nB. Ahead avarege speed.\nC. Move forward at maximum speed.\nD. Halt for the evening.\nE. Execute a status assessment.\nQ. Exit."
    )
    choice = input("What is your choice? ").upper()

    if choice == "Q":
      done = True
      print("\nEnd game\n")

    elif choice == "E":
      print(
          f"\ndistance traveled: {distance_traveled}\nDrinks in canteen: {drinks_in_canteen}\nThirst level: {thirst}\nCamel Tiredness: {camel_tiredness}\nThe natives are {abs(distance_traveled - distance_natives)} miles behind you.\n"
      )

    elif choice == "D":
      camel_tiredness = 0
      print("\nCamel is lucky!\n")
      distance_natives += random_num

    elif choice == "C":
      distance_traveled += random_move
      print(f"\nYou traveled {random_move} miles\n")
      thirst += 1
      camel_tiredness += random_camel_tiredness
      distance_natives += random_num

    elif choice == "B":
      distance_traveled += random_go_ahead
      print(f"\nYou traveled {random_go_ahead} miles\n")
      thirst += 1
      camel_tiredness += 1
      distance_natives += random_num

    elif choice == "A":
      if drinks_in_canteen > 0:
        drinks_in_canteen -= 1
        thirst = 0
        print("\nYou drank from your container.\n")
      else:
        print("\nYou've run out of water.\n")

    if thirst > 4:
      print("\nYou are feeling the need for a drink.\n")
      done = True
      print("\ndied of thirst!\n")
    if camel_tiredness > 5:
      print("\nOur camel is becoming fatigued.\n")
      done = True
      print("\ndied of exhaustion\n")
    if distance_traveled >= 200:
      done = True
      print("\nYou emerged victorious! Well done!\n")

    if random_oasis == 17:
      print(
          "\nYou've discovered an oasis! Your water container is replenished, and your camel is rejuvenated.\n"
      )
      drinks_in_canteen = 3
      camel_tiredness = 0

    if distance_natives >= distance_traveled:
      print("\nThe indigenous people have reached your location!\n")
      done = True
    elif distance_natives + 15 > distance_traveled:
      print("\nThe indigenous people are drawing near!\n")

  print("\nEnd game\n")


main()