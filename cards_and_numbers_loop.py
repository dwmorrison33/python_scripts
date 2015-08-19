
import random

def new_deck():
    x = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    y = range(1, 14)
    z = []
    for suite in x:
        for card_num in y:
            new_card = "%s %s" % (card_num, suite)
            z.append(new_card)
    return z

deck = new_deck()

def make_hand(d):
    hand = []
    for i in range(2):
        length_of_deck = len(d)-1
        rand_index = random.randint(0,length_of_deck)
        card = d.pop(rand_index)
        hand.append(card)
    return hand


set_of_hands = []

for i in range(9):
    set_of_hands.append(make_hand(deck))

for i in set_of_hands:
    print i
