"""
Title: Treasure Island
Author: Michał Chojna
Date: 03.06.2022
Description: Written game in which the goal is to find a treasure
"""

# Prints welcome logo
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************
''')

# Prints welcome message
print("Welcome to the Treasure Island.")

# Prints goal of the game
print("Your mission is to find the treasure")

# Takes the user's decision where to go
if input("You are at a cross road. where do you want to go? Type \"left\" or \"right\". ").lower() == "left":

    # If user's decision where to go is left
    # Takes the user's decision where to go next
    if input("You come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a "
             "boat. Type \"swim\" to swim across. ").lower() == "swim":

        # If user's decision what to go is swim
        # Takes the user's decision which door to choose
        decision = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and "
                         "one blue. Type \"red\" to choose red, type \"yellow\" to choose yellow, type \"blue\" to "
                         "choose blue. Which colour do you choose? ")

        # If user's decision which door to choose is yellow
        if decision.lower() == "yellow":

            # Prints consequence of this decision
            print("You found the treasure! You Win!")

        # If user's decision which door to choose is blue
        elif decision.lower() == "blue":

            # Prints consequence of this decision
            print("You enter a room of beasts. Game Over!")

        # If user's decision which door to choose is blue
        else:

            # Prints consequence of this decision
            print("It is a room full of fire. Game Over!")

    # If user's decision what to do is wait
    else:

        # Prints consequence of this decision
        print("You get attacked by an angry trout. Game Over.")

# If user's decision where to go is right
else:
    # Prints consequence of this decision
    print("You fell into a hole. Game Over.")
