#Higher Lower game
#Compare to randomly selected instagram users and guess who has the most followers
#Will need to pull the names and the follower data for both
import os
import random
import art
import game_data

continue_game = True
score = 0

#example dictonary entry
# {
#     'name': 'Instagram',
#     'follower_count': 346,
#     'description': 'Social media platform',
#     'country': 'United States'
# },

def clear():
    print('\n' * 100)
    os.system('cls' if os.name == 'nt' else 'clear')

def compare_instagram_user(option_1, option_2):
    """Compare the two options and return the option with the highest followers"""
    a = option_1
    b = option_2

    if a["follower_count"] > b["follower_count"]:
        return a
    else:
        return b

def format_data (option):
    """Take the option data and return the printable format"""
    name = option["name"]
    description = option["description"]
    ccountry = option["country"]
    return f"{name}, {description}, from {ccountry}"

option_1 = random.choice(game_data.data)
print(art.logo)
while continue_game:

    option_2 = random.choice(game_data.data)
    if option_2 == option_1:
        option_2 = random.choice(game_data.data)


    print(f"Compare A: {format_data(option_1)}")
    print(art.vs)
    print(f"Compare B:  {format_data(option_2)}")

    selection = input("Who has more follower? Type 'A' or 'B': ").upper()

    if selection == "A":
        answer = option_1
    elif selection == "B":
        answer = option_2

    clear()
    print(art.logo)

    if answer == compare_instagram_user(option_1, option_2):
        option_1 = answer
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        continue_game = False
        print(f"Sorry, that's wrong. Final score: {score}")



