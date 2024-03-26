import random
import os
from art import logo

player_cards = []
dealer_cards = []

playing_blackjack = True

def clear():
    print('\n' * 100)
    os.system('cls' if os.name == 'nt' else 'clear')

def sum_score(hand):
    if sum(hand) == 21 and len(hand) == 2:
        return 0

    if 11 in hand and sum(hand) > 21:
        hand.remove(11)
        hand.append(1)

    return sum(hand)


def check_scores(player_score, dealer_score):
    if player_score == dealer_score:
        print("Draw")
    elif (dealer_score) == 0:
        print("Blackjack! Deal Wins.")
    elif (player_score) == 0:
        print("Blackjack! You Win.")
    elif (player_score) > 21:
        print("Bust. You Lose.")
    elif (dealer_cards):
        print("Deal Bust. You Win!")
    elif (player_score > dealer_score):
        print("You Win")
    else:
        print("You Lose.")

def draw_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def check_draw_card():
    return input(f"Type 'y' to get another card, type 'no' to pass").lower()

while playing_blackjack:
    if (input(f"Do you want to play a game of blackjack? Type 'y' or 'n': ").lower() == 'y'):
        print("Goodbye")
        playing_blackjack = False

    clear()
    print(logo)

    continue_game = True
    player_cards = []
    player_score = -1
    dealer_cards = []
    dealer_score = -1

    for i in range(2):
        player_cards.append(draw_card())
        dealer_cards.append(draw_card())

    while continue_game:

        player_score = sum_score(player_cards)
        dealer_score = sum_score(dealer_cards)

        print(f"    Your cards: {player_cards} current score: {sum_score(player_cards)}")
        print(f"    Dealer's first card: {dealer_cards[0]}")

        print(f"{player_score} , {dealer_score}")
        if player_score == 0 or dealer_score == 0 or player_score > 21:
            print("called")
            continue_game = False
        else:
            player_deal = input(f"Type 'y' to get another card, type 'no' to pass: ").lower()
            if player_deal == 'y':
                player_cards.append(draw_card())
            else:
                continue_game = False


    while dealer_score < 17 and dealer_score != 0:
        dealer_cards.append(draw_card())
        dealer_score = sum_score(dealer_cards)

    print(check_scores(player_score, dealer_score))

