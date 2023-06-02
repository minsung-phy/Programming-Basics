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

# 실습 9.3 카드게임 블랙잭 구현
def blackjack():
    print("Welcome to softopia Casino")
    deck = fresh_deck()
    chips = 0
    while True:
        print("-----")
        dealer = []
        player = []
        card, deck = hit(deck) # 1장 뽑아서
        player.append(card) # 손님에게 주고
        card, deck = hit(deck) # 1장 뽑아서
        dealer.append(card) # 딜러에게 주고
        card, deck = hit(deck) # 1장 뽑아서
        player.append(card) # 손님에게 주고
        card, deck = hit(deck) # 1장 뽑아서
        dealer.append(card) # 딜러에게 준다.
        print("My cards are:")
        print(" ", "****", "**")
        print(" ", dealer[1][0], dealer[1][1])
        show_cards(player, "Your cards are:")
        score_player = count_score(player)
        score_dealer = count_score(dealer)
        if score_player == 21:
            chips += 2
            print("Blackjack! You won.")
        else:
            while score_player < 21 and more("Hit? (y or n) "):
                card, deck = hit(deck) # 1장 뽑아서
                player.append(card) # 손님에게 준다.
                score_player = count_score(player)
                print(" ", card[0], card[1])
            if score_player > 21:
                print("You bust! I won.")
                chips -= 1
            else:
                while score_dealer <= 16:
                    card, deck = hit(deck) # 1장 뽑아서
                    dealer.append(card) # 딜러에게 준다.
                    score_dealer = count_score(dealer)
                show_cards(dealer, "My cards are:")
                if score_dealer > 21:
                    print("I bust! you won.")
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
            if not more("Play more? (y/n) "):
                break
        print("-----")
        print("Bye!")

## 딕셔너리
# 딕셔너리: 프로그래머가 주도적으로 문자열이나 수를 키로 지정할 수 있는 데이터 구조
# 딕셔너리(dict)는 키와 값의 쌍을 모아놓은 것이다. 여기서 키와 값은 서로 짝이 되는 매핑이다. 딕셔너리는 이 키와 값의 매핑을 쉽표(,)로 구분하여 나열하고 전체를 중괄호({,})로 둘러싸 표현한다.
# 딕셔너리는 프로그래머가 키를 문자열 또는 수 등의 수정불가능한 값으로 지정할 수 있다. 딕셔너리 내부에서 키는 인덱스를 사용할 것이므로 당연히 unique 해야 한다.

me = {"이름": "이민성", "생년": 2003, "이메일": "chocomin0211@hanyang.ac.kr"}
print(me)
# 여기서 "이름", "생년", "이메일"은 모두 키이다. 

# 빈 딕셔너리는 다음과 같이 둘 중 하나로 표현할 수 있다.
print({})
print(dict())

# 딕셔너리에서 값 꺼내보기
print(me["이름"])
print(me["생년"])
# 만약 딕셔너리에 없는 키로 꺼내려고 시도하는 경우, 실행오류가 발생한다.
try:
    print(me["취미"])
except KeyError:
    print("딕셔너리에 없는 키로 꺼내려고 시도하는 경우, 실행오류가 발생한다.")
# 라이브러리에서 제공하는 get 메소드를 사용하면, 키로 해당 내부 값을 꺼내볼 수 있을 뿐 아니라 키가 없어도 실행오류가 발생하지 않는다.
print(me.get("취미")) # 키 "취미"가 딕셔너리 me에 있으면 그 값을 리턴하고, 없으면 None을 리턴한다.
print(me.get("취미", "취미가 없습니다")) # 키 "취미"가 딕셔너리 me에 있으면 그 값을 리턴하고, 없으면 "취미가 없습니다"를 리턴한다.
# get 메소드를 사용하면 키가 없어도 KeyError 오류가 발생하지 않으므로 더 안전하다.

# 고치기
# me의 내부 데이터 값을 고치려면, 해당 키를 다음과 같은 요령으로 명시하고 새로운 값을 지정하면 된다.
me["이메일"] = "chocomin0211@gmail.com"
print(me)
# 키가 없으면, 키와 값 쌍을 딕셔너리에 새로 추가한다.
me["취미"] = ["음악듣기", "달리기", "맥주빚기"]
print(me)
# 이 사례에서 보듯이 딕셔너리 내부 데이터의 값에는 제한이 없다. 리스트뿐만 아니라 튜플, 집합, 심지어는 딕셔너리 자신이어도 상관없다.

# 지우기
# 특정 값을 딕셔너리에서 지우려면 del 명령을 사용한다.
del me["취미"]
print(me)
# 만약 딕셔너리에 없는 키로 del 명령을 시도하면 실행오류가 발생한다.
try:
    del me["취미"]
except KeyError:
    print("딕셔너리에 취미 키가 없습니다.")
# 따라서 살행오류를 방지하려면 지우기 전에 키의 존재 여부를 확인해야 한다. 다음 식은 "취미" 키가 me에 없어서 if 블록을 실행하지 않으므로 실행오류가 발생하지 않는다.
if "취미" in me: del me["취미"]

# 딕셔너리 훑기
# 아래 메소드는 키 또는 값 또는 아이템을 리스트로 모아 뷰 객체를 만들어 딕셔너리를 체계적으로 훑어서 계산할 수 있도록 도와준다.
print(me.keys()) # 딕셔너리 me의 키를 리스트로 모아 뷰 객체를 만들어 리턴한다.
print(me.values()) # 딕셔너리 me의 값을 리스트로 모아 뷰 객체를 만들어 리턴한다.
print(me.items()) # 딕셔너리 me의 아이템을 리스트로 모아 뷰 객체를 만들어 리턴한다. 여기서 아이템은 (키, 값) 튜플을 말한다.
for x in me.keys(): print(x)
for x in me.values(): print(x)
for x in me.items(): print(x)
# 뷰 객체로 만들어두면, 딕셔너리의 내부 데이터를 변경하거나 추가하는 경우, 뷰 객체도 연동된다.
my_items = me.items()
for (key, value) in my_items: print(value)
me["키"] = 181 # me에 새로운 아이템을 하나 추가하면, my_item도 연동된다.
print(me)
for (key, value) in my_items: print(value)

# 문자열 메소드
# s.strip(chars): 문자열 s의 양쪽 끝에서 문자열 chars에 있는 문자를 모두 제거하고 리턴한다. 인수가 비어있으면, 빈칸을 모두 제거하고 리턴한다.
# s.split(sep): 구분 문자열 sep을 중심으로 문자열 s를 분리하여 리스트로 모아 리턴한다. 인수가 비어있으면, 빈칸을 구분 문자열로 하여 분리한다.

# 실습 9.4 파일에서 게임 기록 정보 읽기 함수
def load_members():
    file = open("/Users/minsung/Documents/2학년 1학기/프로그래밍기초/기말고사 공부/members.csv", "r")
    members = {}
    for line in file:
        name, passwd, tries, wins, chips = line.strip('\n').split(',')
        members[name] = (passwd, int(tries), float(wins), int(chips))
    file.close()
    return members

# 실습 9.5 파일에 게임 기록 정보 쓰기 함수
def store_members(members):
    file = open("/Users/minsung/Documents/2학년 1학기/프로그래밍기초/기말고사 공부/members.csv", "w")
    names = members.keys()
    for name in names:
        passwd, tries, wins, chips = members[name]
        line = name + ',' + passwd + ',' + str(tries) + ',' + str(wins) + ',' + str(chips) + '\n'
        file.write(line)
    file.close()

# 실습 9.6 로그인 함수
def safe_divide(x, y):
    return x/y if y > 0 else 0

def login(members):
    username = input("Enter your name: (4 letters max) ")
    while len(username) > 4:
        username = input("Enter your name: (4 letters max)")
    trypasswd = input("Enter your password: ")
    if username in members.keys(): 
        if trypasswd == members[username][0]: 
            tries = members[username][1]
            wins = [username][2]
            chips = [username][3]
            print("You played", tries, "games and won", wins, "of them.")
            wpercent = safe_divide(wins, tries) * 100
            print("Your all-time winning percentage is", "{0:.1f}".format(wpercent), "%.")
            if chips > 0:
                print("You have", chips, "chips.")
            else:
                print("You have owe", -chips, "chips.")
            return username, tries, wins, chips, members
        else:
            return login(members)
    else:
        members[username] = (trypasswd, 0, 0, 0)
        return username, 0, 0, 0, members

