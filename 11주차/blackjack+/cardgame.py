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

def load_members():
    file = open("/Users/minsung/Documents/2학년 1학기/프로그래밍기초/11주차/members.csv", "r")
    members = {}
    for line in file:
        name, passwd, tries, wins, chips = line.strip('\n').split(',')
        members[name] = (passwd, int(tries), float(wins), int(chips))
    file.close()
    return members

def store_members(members):
    file = open("/Users/minsung/Documents/2학년 1학기/프로그래밍기초/11주차/members.csv", "w")
    names = members.keys()
    for name in names:
        passwd, tries, wins, chips = members[name]
        line = name + ',' + passwd + ','+ str(tries) + ',' + str(wins) + ',' + str(chips) + '\n'
        file.write(line)
    file.close()

def login(members):
    username = input("Enter your name: (4 letters max) ")
    while len(username) > 4:
        username = input("Enter your name: (4 letters max) ")
    trypasswd = input("Enter your password: ")
    if username in members.keys():
        if trypasswd == members[username][0]():
            tries = members[username][1]
            wins = members[username][2]
            print("You played", tries, "games and won", wins, "of them")
            wpercent = wins / tries * 100 if tries > 0 else 0
            print("Your all-time winning percentage is", "{0:.1f}".format(wpercent), "%")
            chips = members[username][3]
            if chips > 0:
                print("you have", chips, "chips.")
            else:
                print("you owe", -chips, "chips.")
            return username, tries, wins, chips, members
        else:
            return login(members)
    else:
        members[username] = (trypasswd, 0, 0, 0)
        return username, 0, 0, 0, members
    
def show_top5(members):
    print("---")
    sorted_members = sorted(members.items(), key=lambda x: x[1][3], reverse=True)
    print("All-time Top 5 based on the number of chips eaerned")
    rank = 1
    for members in sorted_members[:5]:
        chips = members[1][3]
        if chips <= 0:
            break
    print(rank, ".", members[0], ":", chips)
    rank += 1