
"""
# ***War Game***
# War is a card game designed for two players, utilizing a standard (French style) 52-card deck of playing-cards. 
# The objective is to capture all the cards in the game before your opponent.

# *Gameplay*
# All cards are shuffled, and then divided equally to each player in face down stacks (one stack for each player). 
# Each player reveals the top card of their deck simultaneously, 
# with the player revealing the highest-ranking card winning that particular round and thusly capturing their opponent's card 
# (in addition to retaining their card). Both cards are then returned to the round-winner's deck, placed face down at the bottom. 
# Gameplay continues in the above fashion, with players playing out consecutive rounds, until one player runs out of cards and loses.

# *Rankings*
# Cards are ranked by face value, with Ace, King, Queen, and Jack each (in order) taking the highest ranking, 
# followed by number cards in numerical order (10 being worth more than a 9, etc.).

# *Ties*
# In the event of a tie in a round - two players playing the same ranked cards - both cards are left face up between the two players, 
# and play proceeds to the next round. The winner of the next round takes all cards from the current as well as previous round.

# *Challenge*
# Your challenge is to write an application to simulate a game of War. Play out a game in full, and output the winner. 
# Additionally, outputting the results of each round, including the card that each player played as well as the verdict of which player won. 
# If no winner exists after 100 rounds, the game ends with a prompt to play chess instead.
"""


import random

def play_war():
    # Generate deck of cards
    deck = [n for n in range(2, 15) * 4]

    # Substitute face cards as 11 - 14, retrieve w dict
    faces = {11: 'Jack', 12: 'Queen', 13: 'King', 14: 'Ace'}
    
    # Randomize
    random.shuffle(deck)

    # Split the deck between players
    a_cards = deck[:26]
    b_cards = deck[26:]

    round_count = 1
    tie_cache = [] # Store tie cards here
    
    while a_cards and b_cards:
        if round_count < 100:
            # take from front, append back
            a_card = a_cards.pop(0)
            b_card = b_cards.pop(0)
        
            if a_card > b_card:
                a_cards.append(a_card)
                a_cards.append(b_card)
                
                # check for cached cards from previous round, append, clear cache
                if len(tie_cache) != 0:
                    for c in tie_cache:
                        a_cards.append(c)
                    del tie_cache[:]

                a_card_print = faces.get(a_card, a_card)
                b_card_print = faces.get(b_card, b_card)
                print('Round {0}: {1} beats {2}. Player A wins!'.format(round_count, a_card_print, b_card_print))
            
            elif a_card < b_card:
                b_cards.append(a_card)
                b_cards.append(b_card)
                
                # check for cached cards from previous round, append, clear cache
                if len(tie_cache) != 0:
                    for c in tie_cache:
                        b_cards.append(c)
                    del tie_cache[:]

                a_card_print = faces.get(a_card, a_card)
                b_card_print = faces.get(b_card, b_card)
                print('Round {0}: {1} beats {2}. Player B wins!'.format(round_count, b_card_print, a_card_print))

            elif a_card == b_card:
                tie_cache.append(a_card)
                tie_cache.append(b_card)

                a_card_print = faces.get(a_card, a_card)
                print("Round {0}: It's a tie! Both players had a(n) {1}".format(round_count, a_card_print))

            round_count += 1

        else:
            print('You should play a game of chess instead...')
            break


if __name__ == "__main__":
    play_war()
