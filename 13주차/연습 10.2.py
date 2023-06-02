import random

def fresh_deck():
    suits = {"Spade", "Heart", "Diamond", "Club"}
    ranks = {2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"}
    deck = []
    for s in suits:
        for r in ranks:
            card = (s, r)
            deck.append(card)
    random.shuffle(deck)
    return deck

def hit(deck):
    if deck == []:
        deck = fresh_deck()
    return (deck[0], deck[1:])

def count_score(cards):
    score = 0
    number_of_ace = 0
    for card in cards:
        rank = card[1]
        if rank == 'A':
            score += 11
            number_of_ace += 1
        elif rank in {'J','Q','K'}:
            score += 10
        else:
            score += rank
    while score > 21 and number_of_ace > 0:
        score -= 10
        number_of_ace -= 1
    return score

def show_cards(cards, message):
    print(message)
    for card in cards:
        print(' ', card[0], card[1])

def more(message):
    answer = input(message)
    while not (answer == 'y' or answer == 'n'):
        answer = input(message)
    return answer == 'y'

def blackjack():
    print("Welcome to Softopia Casino")
    deck = fresh_deck()
    chips = 0
    while True:
        print("-----")
        dealer = []
        player = []
        card, deck = hit(deck)  # 1장 뽑아서
        player.append(card)  # 손님에게 주고
        card, deck = hit(deck)  # 1장 뽑아서
        dealer.append(card)  # 딜러에게 주고
        card, deck = hit(deck)  # 1장 뽑아서
        player.append(card)  # 손님에게 주고
        card, deck = hit(deck)  # 1장 뽑아서
        dealer.append(card)  # 딜러에게 준다.
        print("My cards are:")
        print(" ", "", "**")
        print(" ", dealer[1][0], dealer[1][1])
        show_cards(player, "Your cards are:")
        score_player = count_score(player)
        score_dealer = count_score(dealer)
        if score_player == 21:
            chips += 2
            print("Blackjack! You won.")
        else:
            while score_player < 21:
                while True:
                    try:
                        select = input("Hit? (y/n) ")
                        assert select in {"y", "n"}
                    except AssertionError:
                        print("Write y or n.")
                    else:
                        if select == "y":
                            card, deck = hit(deck)  # 1장 뽑아서
                            player.append(card)  # 손님에게 준다.
                            score_player = count_score(player)
                            print(" ", card[0], card[1])
                            if score_player >= 21:
                                break
                        else:
                            break
                if select == "n":
                    break
            if score_player > 21:
                print("You bust! I won.")
                chips -= 1
            else:
                while score_dealer <= 16:
                    card, deck = hit(deck)  # 1장 뽑아서
                    dealer.append(card)  # 딜러에게 준다.   
                    score_dealer = count_score(dealer)
                show_cards(dealer, "My cards are:")
                if score_dealer > 21:
                    print("I bust! You won.")
                    chips += 1
                elif score_dealer == score_player:
                    print("We draw.")
                elif score_dealer < score_player:
                    print("You won.")
                    chips += 1
                else:
                    print("I won.")
                    chips -= 1
        print("Chips =", chips)
        while True:
            try:
                select2 = input("Play more? (y/n)")
                assert select2 in {"y", "n"}
            except AssertionError:
                print("Write y or n.")
            else:
                if select2 == "y":
                    break
                else:
                    print("-----")
                    print("Bye!")
                    return

blackjack()