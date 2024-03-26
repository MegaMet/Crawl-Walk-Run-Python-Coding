import random
import hangman_art
import hangman_words

stages = hangman_art.stages

#Word list to choose form.
word_list = ["aardvark", "baboon", "camel"]
lives = len(stages) - 1

#Select a randomm word.
selected_word = random.choice(hangman_words.word_list)
display_word = []

for i in selected_word:
    display_word.append("_")

print(f"The selected word is: {selected_word}")
#Display the same number of blanks as the the selected word.

game_end = False

#function for displaying hangman
def display_hangman():
    print(f"{stages[lives]}{display_word}")

print(hangman_art.logo)
display_hangman()
while not game_end:
    #Have the user guess a letter and replace the blank spaces of "display_word" with the guessed letter.
    guessed_letter = input("Please guess a letter: ").lower()
    for l in range(len(selected_word)):
        if selected_word[l] == display_word:
            print("The selected letter was already used")
        elif selected_word[l] == guessed_letter:
            display_word[l] = guessed_letter

    #end the game if blank spaces are gone
    if "_" not in display_word:
        game_end = True

    #remove a life and end the game if the lives are 0
    if guessed_letter not in selected_word:
        print("The selected letter was not in the word")
        lives -= 1
        if lives == 0:
            game_end = True

    display_hangman()

#display win or lose
if lives == 0:
    print("You Lose")
else:
    print("You Win")