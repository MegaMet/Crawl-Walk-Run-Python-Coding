import os
import art

bidders = {}
end_bid = False

#Hacky way to clear console in pycharm
def clear():
    print('\n' * 100)
    os.system('cls' if os.name == 'nt' else 'clear')

def find_highest_bidder(bidding_record):
    highest_bidder = ""
    highest_bid = 0
    for bidder in bidding_record:
        if bidding_record[bidder] > highest_bid:
            highest_bid = bidding_record[bidder]
            highest_bidder = bidder

    print(f"The highest bidder is {highest_bidder} with ${highest_bid}")


print(art.logo)
print("Welcome to the secret auction program.")
while not end_bid:
    bidder_name = input("What is your name?: ").capitalize()
    bidder_bid = int(input("What is your bid?: $"))
    bidders[bidder_name] = bidder_bid

    continue_bid = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    if (continue_bid == 'no' or continue_bid == 'n'):
        end_bid = True
    elif (continue_bid == 'ues' or continue_bid == 'y'):
        clear()

find_highest_bidder()



