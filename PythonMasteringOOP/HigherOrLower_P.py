"""Procedural Programming that gets 8 random cards from a deck
    and show the first card then the user guesses if the next
    card has a higher or lower value than the first card"""
import random

SUIT_TUPLE: tuple = ('Spades', 'Hearts', 'Clubs', 'Diamonds')
RANK_TUPLE: tuple = ('Ace', '2', '3', '4', '5', '6', '7', '8',
                     '9', '10', 'Jack', 'Queen', 'King')

N_CARDS_TO_GUESS: int = 8
Score = 50


def get_cards(deck_list_in):
    this_card = deck_list_in.pop()
    return this_card


def shuffle_deck(deck_list_in):
    deck_list_out = deck_list_in.copy()
    random.shuffle(deck_list_out)
    return deck_list_out


def age_denied():
    print('\nYou are not legible to play')
    exit()


if __name__ == '__main__':
    user_n = input('Type your user name: ')
    user_age = int(input('Type your age: '))
    age_denied() if user_age < 5 else 0

    print(f'WELCOME TO HIGHER OR LOWER {user_n}!\nYou have to choose '
          'whether the next card to be shown\nis higher or lower '
          'than the current card shown')
    print('\nGetting the answer right will give you 20 PTS\n'
          'Getting the answer wrong will lose you 15 PTS\n'
          'You have 50 PTS to start\n')

    starting_deck_list = []
    for suit in SUIT_TUPLE:
        for this_value, rank in enumerate(RANK_TUPLE):
            card_dict = {'rank': rank, 'suit': suit, 'value': this_value + 1}
            starting_deck_list.append(card_dict)

    while True:  # play multiple games
        print()
        gameDeckList = shuffle_deck(starting_deck_list)
        current_card_dict = get_cards(gameDeckList)
        current_card_rank = current_card_dict['rank']
        current_card_value = current_card_dict['value']
        current_card_suit = current_card_dict['suit']
        print('Starting card is:', current_card_rank + ' of ' + current_card_suit)
        print()

        for cardNumber in range(0, N_CARDS_TO_GUESS):  # play one game of this many cards
            answer = input('Will the next card be higher or lower than the ' +
                           current_card_rank + ' of ' +
                           current_card_suit + '?  (enter h or l): ')
            answer = answer.casefold()  # force lower case
            nextCardDict = get_cards(gameDeckList)
            nextCardRank = nextCardDict['rank']
            nextCardSuit = nextCardDict['suit']
            nextCardValue = nextCardDict['value']
            print('Next card is:', nextCardRank + ' of ' + nextCardSuit)

            if answer == 'h':
                if nextCardValue > current_card_value:
                    print('You got it right, it was higher')
                    Score += 20
                else:
                    print('Sorry, it was not higher')
                    Score -= 15

            elif answer == 'l':
                if nextCardValue < current_card_value:
                    Score += 20
                    print('You got it right, it was lower')

                else:
                    Score -= 15
                    print('Sorry, it was not lower')

            print('Your score is:', Score)
            print()
            currentCardRank = nextCardRank
            currentCardValue = nextCardValue
            currentCardSuit = nextCardSuit

        goAgain = input('To play again, press ENTER, or "q" to quit: ')
        if goAgain == 'q':
            break

    print('OK bye')
    print(f'{starting_deck_list}\n\n{len(starting_deck_list)}')
