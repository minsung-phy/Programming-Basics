import random

def fresh_deck():
    suits = { "Spade", "Heart", "Diamond", "Club" }
    ranks = { 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "K", "Q", "A" }
    deck = []
    for s in suits:
        for r in ranks:
            card = (s, r)
            deck.append(card)
    random.shuffle(deck)
    return deck

print(fresh_deck())