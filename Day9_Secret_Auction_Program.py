import os

# Clear screen command based on the operating system
def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

from art import *
print(logo)

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder, bid_amount in bidding_record.items():
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
    name = input("What is your name?")
    price = input("What is your bid? $")

    if name and price:  # Kontrollib, et nimi ja hind ei ole tühjad
        bids[name] = int(price)
    else:
        print("Please add your name and bid.")
        continue

    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    
    if should_continue.lower() == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue.lower() == "yes":
        clear()
