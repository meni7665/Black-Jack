import os
import random

# create deck
deck = []
card_type = ['Diamond', 'Heart', 'Spade', 'Clubs']
card_number = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
for c in card_type:
    for n in card_number:
        deck.append([c, n])


# gives the players/dealer 2 cards
def deal(deck):
    hand = []
    random.shuffle(deck)
    for i in range(2):
        hand.append(deck.pop())
    return hand


# resets the game and run again if the player want to
def play_again():
    print('Do you want to play again? Press (Y) or (N)')
    choice = input().lower()
    while choice != 'n' and choice != 'y':
        print('Please press (Y) or (N)')
        choice = input().lower()
    if choice == 'n':
        print('Bye Bye')
        exit()
    if choice == 'y':
        return True


# calculate the sum of cards
def total(hand):
    sumOfCards = 0
    for card in hand:
        if card[1] == 'J' or card[1] == 'Q' or card[1] == 'K':
            sumOfCards += 10
        elif card[1] == 'A':
            sumOfCards += 11
        else:
            sumOfCards += int(card[1])
    if sumOfCards > 21:
        for card in hand:
            if card[1] == 'A':
                sumOfCards -= 10
            continue
    return sumOfCards


# take another card
def hit(hand):
    hand.append(deck.pop())
    return hand


# clear the terminal screen
def clear():
    if os.name == 'nt':
        os.system('CLS')


def print_result(dealer_hand, player_hand):
    print("Player: ", total(player_hand), end='\n')
    print("Dealer: ", total(dealer_hand), end='\n')


# check if one of the players have 21
def blackjack(dealer_hand, player_hand):
    player_result = total(player_hand)
    dealer_result = total(dealer_hand)
    if player_result == 21 and dealer_result == 21:
        print('it\'s a Draw', end='\n')
        return True
    elif player_result == 21:
        print('BlackJack, player won.', end='\n')
        return True
    return False


# all the options of win / lose
def score(dealer_hand, player_hand):
    player_result = total(player_hand)
    dealer_result = total(dealer_hand)
    if player_result > dealer_result:
        print('Congratulation! You win\n')
    elif player_result < dealer_result:
        print('Sorry, you lose.\n')
    else:
        print_result(dealer_hand, player_hand)
        print('Its a draw please play again\n')


# welcome screen
def game():
    choice = ''
    print('Welcome to Cohanov Casino, let\'s play BlackJack')
    player_hand = deal(deck)
    dealer_hand = deal(deck)
    print_result(dealer_hand, player_hand)
    if blackjack(dealer_hand, player_hand):
        return
    while choice != 'q':
        print('Do you want to [H]it, [S]tand, or [Q]uit?', end='\n')
        player_total = total(player_hand)
        if player_total < 21:
            choice = input().lower()
            while choice != 'h' and choice != 's' and choice != 'q':
                print('Do you want to [H]it, [S]tand, or [Q]uit?', end='\n')
                choice = input().lower()
        elif player_total == 21:
            choice = 's'
        if choice == 'h':
            player_hand = hit(player_hand)
            player_total = total(player_hand)
            print_result(dealer_hand,player_hand)
            if player_total > 21:
                print('Sorry, you lose.', end='\n')
                return
        if choice == 's':
            dealer_total = total(dealer_hand)
            while dealer_total < 17:
                dealer_hand = hit(dealer_hand)
                dealer_total = total(dealer_hand)
                print_result(dealer_hand, player_hand)
            if dealer_total > 21:
                print('Congratulations!, you won', end='\n')
                return
            score(dealer_hand, player_hand)
            return

    print('Bye Bye')
    exit()


if __name__ == "__main__":
    restart = 1
    while restart:
        game()
        restart = play_again()
        if restart:
            deck = []
            for i in card_type:
                for j in card_number:
                    deck.append([i, j])
