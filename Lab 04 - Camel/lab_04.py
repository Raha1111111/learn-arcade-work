
import random
def main():
  done = False
  miles_traveled = 0
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
        "\nA. Drink from your canteen.\nB. Ahead moderate speed.\nC. Ahead full speed.\nD. Stop for the night.\nE. Status check.\nQ. Quit."
    )
    choice = input("What is your choice? ").upper()

    if choice == "Q":
      done = True
      print("\nGame Over\n")

    elif choice == "E":
      print(
          f"\nMiles traveled: {miles_traveled}\nDrinks in canteen: {drinks_in_canteen}\nThirst level: {thirst}\nCamel Tiredness: {camel_tiredness}\nThe natives are {abs(miles_traveled - distance_natives)} miles behind you.\n"
      )

    elif choice == "D":
      camel_tiredness = 0
      print("\nCamel is happy!\n")
      distance_natives += random_num

    elif choice == "C":
      miles_traveled += random_move
      print(f"\nYou traveled {random_move} miles\n")
      thirst += 1
      camel_tiredness += random_camel_tiredness
      distance_natives += random_num

    elif choice == "B":
      miles_traveled += random_go_ahead
      print(f"\nYou traveled {random_go_ahead} miles\n")
      thirst += 1
      camel_tiredness += 1
      distance_natives += random_num

    elif choice == "A":
      if drinks_in_canteen > 0:
        drinks_in_canteen -= 1
        thirst = 0
        print("\nYou drank from your canteen.\n")
      else:
        print("\nYou have no water left!\n")

    if thirst > 4:
      print("\nYou are thirsty!\n")
    if camel_tiredness > 5:
      print("\nYour camel is getting tired!\n")

    if miles_traveled >= 200:
      done = True
      print("\nYou won! Congratulations!\n")

    if random_oasis == 17:
      print(
          "\nYou found an oasis! Your canteen is refilled, and your camel is rested.\n"
      )
      drinks_in_canteen = 3
      camel_tiredness = 0

    if distance_natives >= miles_traveled:
      print("\nThe natives caught up to you!\n")
      done = True
    elif distance_natives + 15 > miles_traveled:
      print("\nThe natives are getting closer!\n")

  print("\nGame Over\n")


main()