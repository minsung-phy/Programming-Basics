# 집합 set: 순서와 중복 없이 데이터 값을 모아놓을 수 있는 컬렉션 데이터 구조

# 집합은 구성원소를 쉽표로 구분하여 나열하고 중괄호로 둘러싸 다음과 같이 표현
print({7+8, 8.15, "seven"})

# 집합을 표현한 식과 인터프리터가 계산하여 보여준 결과를 비교해보면 원소 나열 순서가 일치하지 않는다. 집합은 순서를 무시하므로 그래도 상관이 없다.
# 다음 비교 논리식의 계산 결과로 확인할 수 있다.
print({7+8, 8.15, "seven"} == {8.15, "seven", 9+6})

# 집합도 아래와 같이 변수를 지정할 수 있으며, 값의 모음이므로 아래 사례에서 보듯이 시퀀스와 공유하는 함수와 연산이 있다.
myset = {8.15, "seven", 15}
print(len(myset))
print(15 in myset)
for e in myset:
    print(e)

# 하지만 원소에 순서를 매기지 않으므로 인덱스 관련 연산은 없다. 

# 다음 사례에서 볼 수 있듯이 집합 내에서 중복되는 원소는 무시한다. 집합은 중복을 허용하지 않으니 당연하다.
print({2,3,3,4,3,3,3,3})
print(len({2,3,3,4,3,3,3,3}))
print({2,3,3,4,3,3,3,3} == {2,3,4})

# 공집합은 set()로 표현한다.
print(set())

# 집합은 객체로 취급하며, 대표적인 메소드 두 개만 살펴보면 다음과 같다.
# s.add(n): 집합 s에 원소 n을 추가한다.
# s.remove(n): 집합 s에서 원소 n을 제거한다. s에 n이 없으면 KeyError오류(없는 키를 사용한 경우 발생하는 오류)가 발생한다.
positions = set()
positions.add((3,2))
positions.add((0,3))
positions.add((1,2))
print(positions)
positions.add((1,2))
print(positions)
positions.remove((0,3)) # 집합에 없는 원소를 제거하려고 시도하였으므로 KeyError 오류가 발생하였다. 
print(positions)
try:
    positions.remove((5, 5))
except KeyError:
    print("KeyError")

# 실습 9.1 fresh_deck 함수 만들기
import random
def fresh_deck():
    suits = {"Spade", "Heart", "Diamond", "Club"}
    ranks = {2,3,4,5,6,7,8,9,10,"J","Q","K","A"}
    deck = []
    for s in suits:
        for r in ranks:
            card = (s,r)
            deck.append(card)
    random.shuffle(deck)
    return deck

# 카드 덱에서 카드 한 장 뽑아주기
def hit(deck):
    if deck == []:
        deck = fresh_deck()
    return (deck[0], deck[1:])

# 실습 9.2 count_score 함수 만들기
## 나의 답
def count_score(cards):
    score = 0
    number_of_ace = 0
    for card in cards:
        rank = card[1]
        if rank == "A":
            rank = 11
        elif rank in ("J", "Q", "K"):
            rank = 10
        else:
            rank = card[1]
        score += rank
    if score > 21:
        score -= 10
    return score

## 솔루션
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

# 카드 프린트해서 보여주기
def show_cards(cards, message):
    print(message)
    for card in cards:
        print(' ', card[0], card[1])

# 카드를 더 받을지 물어보기
def more(message):
    answer = input(message)
    while not (answer == 'y' or answer == 'n'):
        answer = input(message)
    return answer == 'y' # answer이 y이면 true를 return, n이면 false를 return



