import random
from art import logo


def draw_a_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = cards[random.randint(0, len(cards) - 1)]
    return card


def compare(user_score, computer_score):
    if user_score == 21:
        return "Blackjack, you win!"
    elif user_score > 21:
        return "You bust, computer wins!"
    elif user_score == computer_score:
        return "Draw!"
    elif computer_score == 21:
        return "You lose Computer has Blackjack"
    elif computer_score > 21:
        return "Computer busts, you win!"
    elif user_score > computer_score:
        return "You win!"
    else:
        return "You lose!"


def game():
    user_cards = []
    pc_cards = []
    user_num_of_cards = 2
    for i in range(0, user_num_of_cards):
        user_cards.append(draw_a_card())
    for i in range(0, 2):
        pc_cards.append(draw_a_card())
    while sum(pc_cards) != 21 and sum(pc_cards) < 15:
        pc_cards.append(draw_a_card())

    should_continue = True
    while should_continue:
        if 11 in user_cards and sum(user_cards) > 21:
            user_cards.remove(11)
            user_cards.append(1)
        print(f"Your cards: {user_cards}")
        print(f"Computer's first card: {pc_cards[0]}")
        if sum(user_cards) > 21 or sum(user_cards) == 21 or sum(pc_cards) == 21:
            should_continue = False
        else:
            user_response = input("Type 'y' to get another card, type 'n' to pass\n")
            if user_response == "y":
                user_cards.append(draw_a_card())
            else:
                should_continue = False
    print("\n------END OF GAME------")
    print(f"Your final cards: {user_cards}")
    print(f"Computer's final cards: {pc_cards}")
    print(compare(sum(user_cards), sum(pc_cards)))


play = input("Do you want to play a game of Blackjack, type 'y' for yes\n")
should_play = True
if play == "y":
    should_play = True
else:
    should_play = False

while should_play:
    print(logo)
    game()
    play = input("Do you want to play another game of Blackjack, type 'y' for yes\n")
    if play == 'y':
        should_play = True
    else:
        should_play = False





