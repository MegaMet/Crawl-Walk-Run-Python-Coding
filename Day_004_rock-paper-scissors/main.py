import random

# Rock
rock=("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
paper=("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
scissors=("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

selection = [rock, paper, scissors]

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors\n"))
computer_choice = random.randint(0, 2)

print(f"{selection[player_choice]}\nComputer chose:\n{selection[computer_choice]}")

if (player_choice == computer_choice):
    print("Draw")
elif ((player_choice == 0 and computer_choice == 2) or
      (player_choice == 1 and computer_choice == 0) or
      (player_choice == 2 and computer_choice == 1)):
    print("You Win")
else:
    print("You lose")