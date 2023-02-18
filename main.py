TwentyOne = 21
age = int(input("how old are you? "))
if age < TwentyOne:
    kids_menu = ["Cookie", "Chocolate", "Candy"]
    print("Okay, you can have the kids menu.")
    print("The kids menu has " + ", ".join(kids_menu))
    choice = input("What would you like to order? ")
    while choice not in kids_menu:
        print("Sorry, that's not on the menu.")
        choice = input("Please choose an item from the menu: ")
    print("Great choice! Enjoy your " + choice + ".")
else:
    adult_menu = ["Steak", "Salmon", "Pasta"]
    print("Time to party!")
    print("Here's the adult menu: " + ", ".join(adult_menu))
    choice = input("What would you like to order? ")
    while choice not in adult_menu:
        print("Sorry, that's not on the menu.")
        choice = input("Please choose an item from the menu: ")
    print("Excellent choice! Enjoy your " + choice + ".")
first_name = input("what's your first name? ")
last_name = input("what's your last name? ")
print("Hello " + first_name + " " + last_name + "have a nice day")
answer = input ("how are you")
if answer == ("good") or ("Good"):
  print("thats good")
if answer == ("bad") or ("Bad"):
  print("I hope you feel better")
if first_name.lower() == "bus":
    print("That's not your name.")


