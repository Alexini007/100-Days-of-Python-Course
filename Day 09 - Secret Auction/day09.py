import art
from replit import clear

print(art.logo)

bids = {}
biding_finished = True

def highest_bid(bids):
    winner = ""
    current_max = 0
    for bid in bids:
        if current_max < bids[bid]:
            current_max = bids[bid]
            winner = bid
    print(f"\nTHe winner of the auction is {winner} with a bid of ${current_max}")


while biding_finished:
    name = input("What is your name\n")
    bid = int(input("What is your bid?\n"))
    bids[name] = bid
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n")

    if should_continue == "no":
        biding_finished = False
        highest_bid(bids)
        clear()

