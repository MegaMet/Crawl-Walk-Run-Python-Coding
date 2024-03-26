#Provide opening message
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
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')

print("Welcome to Tresure Island.\nYour missing is to find the treasure.")
#Provide the user with the first choice and determine if they continue or loose.
choice_one = input("""You're at a cross road. Where do you want to go? Type "left" or "right"\n""")
if (choice_one == "left"):
    #Provide the user with the second choice of swimming or waiting.
    choice_two = input("""You come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across\n""")
    if (choice_two == "wait"):
        #Procide the user with the third choice of doors and determine the end of their adventure
        choice_three = input("""You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, and one blue. Which color do you choose?\n""")
        if (choice_three == "red"):
            print("It's a room full of fire and you became BBQ. Game Over")
        elif (choice_three == "blue"):
            print("You entered a room full of beast and were eaten alive. Game Over")
        elif (choice_three == "yellow"):
            print("You found the treasure! You Win!")
        else:
            print("You took to long to decide and were squashed by a bolder. Game over.")
    elif (choice_two == "swim"):
        print("You were attack by an swam of ducks. Game over.")
    else:
        print("You chose to do neither and the island exploded. Game over.")
elif (choice_one == "right"):
    print("You fell into a hole and become discourage. Game Over")
else:
    print("You remember that you aren't good at spelling and lost interest in the treasure. Game over.")
