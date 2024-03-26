## Number Guessing game
import random

number_of_guess = 0
selected_number = 0

def set_difficulty_level():
    difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty_level == 'easy':
        return 10
    elif difficulty_level == 'hard':
        return 5

def check_number(guessed_number):
    global number_of_guess
    if guessed_number == selected_number:
        print(f"You got it! The answer was {selected_number}.")
        number_of_guess = 0
    elif guessed_number > selected_number:
        print("Too high\nGuess again.")
        number_of_guess -= 1
    elif guessed_number < selected_number:
        print("Too low\nGuess again.")
        number_of_guess -= 1

selected_number = random.randrange(1, 101)

number_of_guess = set_difficulty_level()

while number_of_guess > 0:
    print(f"You have {number_of_guess} attempt remaining to guess the number")
    guessed_number = int(input("Make a guess: "))
    check_number(guessed_number)