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

card1 = [('Club', 4), ('Spade', 10) ,('Diamond', 'J'), ('Diamond', 'A')]
card2 = [('Spade', 10)]
card3 = [('Diamond', 'J')]
card4 = [('Diamond', 'A')]

print(count_score(card1))
print(count_score(card2))
print(count_score(card3))
print(count_score(card4))