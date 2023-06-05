# 실습 10.1 예외 발생시켜 보기

## ValueError
try:
    num = int("python")
except ValueError:
    print("ValueError")

## IndexError
try:
    a = ['a', 'b', 'c', 'd', 'e']
    a[50]
except IndexError:
    print("IndexError")

## KeyError
try:
    me = {"name": "이민성", "bir": "2003", "email": "chocomin0211@hanyang.ac.kr"}
    phonenum = me["phonenum"]
except KeyError:
    print("KeyError")

# 예외 처리 제어 구조
while True:
    try:
        x = int(input("Enter a number: "))
        reciprocal = 1 / x
        print("The reciprocal of", x, "is", reciprocal)
        break
    except ValueError:
        print("Not a number.")
    except ZeroDivisionError:
        print("The reciprocal of 0 does not exist.")
        break

## 두 종류 이상의 예외에 대해서 동일한 방식으로 처리하고 싶으면 예외 이름을 다음과 같이 튜플로 묶어 둔다.
try:
    pass
except (ValueError, TypeError, NameError):
    pass

## 예외 이름을 생략한 무명 except 블록을 다음 코드와 같이 맨 뒤에 둘 수 있다.
while True:
    try:
        x = int(input("Enter a number: "))
        reciprocal = 1 / x
        print("The reciprocal of", x, "is", reciprocal)
        break
    except ValueError:
        print("Not a number.")
    except ZeroDivisionError:
        print("The reciprocal of 0 does not exist.")
        break
    except:
        print("Unexcepted exception occurred.")
        break

## 발생한 예외는 오류 메시지를 소지하고 있는데, 아래 코드와 같은 형식으로 예외 이름 뒤에 as 키워드와 변수를 나랑히 언급하여 소지한 메세지를 전달 받을 수 있다.
while True:
    try:
        x = int(input("Enter a number: "))
        reciprocal = 1 / x
        print("The reciprocal of", x, "is", reciprocal)
        break
    except ValueError as message:
        print(message)
    except ZeroDivisionError as message:
        print(message)
        break

## 맨 뒤에 선택사양으로 else 블록을 추가할 수도 있다. else 블록은 예외가 발생하지 않은 경우에만 실행한다. 아래는 이전 코드의 try 블록의 후반 두 줄을 else 블록으로 옮긴 코드이다.
## try 블록에서 예외가 발생하지 않은 경우에 실행할 부분이므로 else 블록으로 이동해도 실행 의미가 동일하다.
while True:
    try:
        x = int(input("Enter a number: "))
        reciprocal = 1 / x
    except ValueError:
        print("Not a number.")
    except ZeroDivisionError:
        print("The reciprocal of 0 does not exist.")
        break
    else:
        print("The reciprocal of", x, "is", reciprocal)
        break
    finally:
        print(":-)")
## 이전 코드와 실행 결과는 다르지 않다. 하지만 이 경우 try 블록에서 예외가 발생할 경우와 그렇지 않은 경우를 같은 수준에서 표현하여 코드의 가독성을 높이는 장점이 있다.
## 맨 뒤에 선택사양으로 finally 블록을 추가할 수도 있다. finally 블록은 예외 발생 여부에 상관없이 무조건 실행한다. 

# 실습 10.2 실수 입력 확인
def input_float():
    while True:
        try:
            f = float(input("Enter a float number: "))
        except ValueError:
            print("실수를 입력하세요.")
        else:
            print(f)
            break

# assert문: 주어진 조건을 만족하지 않으면 AssertionError 예외를 발생시키는 문장
def fac(n):
    ans = 1
    while n > 1:
        ans = n * ans
        n = n - 1
    return ans

def factorial():
    while True:
        try:
            n = int(input("Enter a number: "))
            assert n >= 1
        except ValueError:
            print("Not a number.")
        except AssertionError:
            print("Not a natural number.")
        else:
            print("factorial(", n, ") = ", fac(n), sep='')
            print("Goodbye!")
            break

# 실습 10.3 조합 계산 서비스 구현
def comb_pascal(n, r):
    row0 = [1 for _ in range(r+1)]
    matrix = [row0] + [[1] for _ in range(n-r)]
    for i in range(1, n - r + 1):
        for j in range(1, r + 1):
            newvalue = matrix[i][j - 1] + matrix[i - 1][j]
            matrix[i].append(newvalue)
    return matrix[n - r][r]

def ncr():
    print("This program computes combination of two natural numbers, n and r.")
    print("press Control+C to quit.")
    while True:
        try:
            n = int(input("Enter n : "))
            r = int(input("Enter r : "))
            assert n, r >= 0 
            assert r <= n
        except ValueError:
            print("Must be a number")
        except AssertionError:
            print(n, "C", r, " is not defined.", sep='')
        except KeyboardInterrupt:
            print("Goodbye!")
            break
        else:
            print(n, "C", r, " = ", comb_pascal(n, r), sep='')

# 사용자 정의 예외: 프로그래머의 필요에 의해서 만드는 예외
## 프로그램 실행 중에 프로그램 내부에서 발생하는 모든 예외를 대표하는 이름은 Exception이다. 외부 요인으로 발생하는 예외 몇 개를 제외하고 내장 예외는 모두 Exception 소속이다.
## 필요한 경우 Exception 소속으로 얼마든지 새로운 예와를 만들 수 있다. 
## 예를 들어 앞에서 살펴본 팩토리얼 사례에서 정수 인수가 양수가 아닌 예외를 처리할 용도로 NonPositive라는 이름의 새로운 예외를 다음과 같이 하나 새로 정의할 수 있다.
## class NonPositive(Exception): pass
## 그러면 양수가 아닌 정수를 만났을 때, raise NonPositive라 언급하면 NonPositive 예외가 발생한다. 
class NonPositive(Exception): pass
def factorial():
    while True:
        try:
            n = int(input("Enter a number: "))
            if n < 1:
                raise NonPositive
        except ValueError:
            print("Not a number.")
        except NonPositive:
            print("Not a natural number.")
        else:
            print("factorial(", n, ") = ", fac(n), sep='')
            print("Goodbye!")
            break

# 실습 10.4 실수 입력 확인(범위 제한)
class OutRange(Exception): pass

def input_float_one():
    while True:
        try:
            f = float(input("Enter a float number: "))
            if not(-1.0 <= f <= 1.0):
                raise OutRange
        except ValueError:
            print("실수를 입력하세요.")
        except OutRange:
            print("Range is '-1.0 <= f <= 1.0'.")
        else:
            print(f)
            break

# 연습 10.1 퍼즐 게임 미니 스도쿠 예외 처리 추가
import random
import time

def initialize_board_4x4(): 
    row0 = [1,2,3,4]
    random.shuffle(row0)
    row1 = row0[2:4] + row0[0:2]
    row2 = [row0[1],row0[0],row0[3],row0[2]]
    row3 = row2[2:4] + row2[0:2]
    return [row0, row1, row2, row3]

def shuffle_ribbons(board):
    top = board[:2]
    bottom = board[2:]
    random.shuffle(top)
    random.shuffle(bottom)
    return top + bottom

def transpose(board):
    size = len(board)
    transposed = [[] for _ in range(size)]
    for row in board:
        for i in range(size):
            transposed[i].append(row[i])
    return transposed

def create_solution_board_4x4():
    board = initialize_board_4x4()
    board = shuffle_ribbons(board)
    board = transpose(board)
    board = shuffle_ribbons(board)
    board = transpose(board)
    return board

def copy_board(board):
    board_clone = []
    for row in board:
        board_clone.append(row[:])
    return board_clone

def get_level():
    print("Enter your level.")
    level = input("Beginner=1, Intermediate=2, Advanced=3: ")
    while level not in ("1","2","3"):
        level = input("Beginner=1, Intermediate=2, Advanced=3: ")
    if level == "1":
        return 6
    elif level == "2":
        return 8
    else:
        return 10
    
def make_holes(board, no_of_holes):
    while no_of_holes > 0:
        i = random.randint(0,3)
        j = random.randint(0,3)
        if board[i][j] != 0:
            board[i][j] = 0
            no_of_holes -= 1  
    return board

def show_board(board):
    for row in board:
        for entry in row:
            if entry == 0:
                print('.', end=' ')
            else:
                print(entry, end=' ')
        print()

def sudoku_4x4():
    solution_board = create_solution_board_4x4()
    puzzle_board = copy_board(solution_board)
    no_of_holes = get_level()
    puzzle_board = make_holes(puzzle_board, no_of_holes)
    show_board(puzzle_board)
    start = time.time()
    while no_of_holes > 0:
        while True:
            try:
                i = int(input("Row#(1,2,3,4): ")) - 1
                j = int(input("Column#(1,2,3,4): ")) - 1
                assert 0 <= i <= 3
                assert 0 <= j <= 3
            except ValueError:
                print("Not a number.")
            except AssertionError:
                print("Not in a range. (range : '1 <= row, column <= 4')")
            else:
                if puzzle_board[i][j] != 0:
                    print("Not empty!")
                    continue
                while True:
                    try:
                        n = int(input("Number(1,2,3,4): "))
                        assert 1 <= n <= 4
                    except ValueError:
                        print("Not a number.")
                    except AssertionError:
                        print("Not in a range. (range : '1 <= Number <= 4')")
                    else:
                        if n == solution_board[i][j]:
                            puzzle_board[i][j] = solution_board[i][j]
                            show_board(puzzle_board)
                            no_of_holes -= 1
                        else:
                            print(n, ": Wrong number! Try again.")
                        break
                    break
                break
    end = time.time()
    print("It took you", round(end - start, 2), "seconds to complete the game.")
    print("Well done! Come again.")

# 연습 10.2 카드게임 블랙잭 예외 처리 추가
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

def blackjack():
    print("Welcome to Softopia Casino")
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
            while score_player < 21:
                while True:
                    try:
                        select = input("Hit? (y/n) ")
                        assert select in ["y", "n"]
                    except AssertionError:
                        print("Write y or n.")
                    else:
                        if select == "y":
                            card, deck = hit(deck) # 1장 뽑아서
                            player.append(card) # 손님에게 준다.
                            score_player = count_score(player)
                            print(" ", card[0], card[1])
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
                    card, deck = hit(deck) # 1장 뽑아서
                    dealer.append(card) # 딜러에게 준다.   
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
                select2 = input("Play more? (y/n) ")
                assert select2 in ["y", "n"]
            except AssertionError:
                print("Write y on n.")
            else:    
                break
        if select2 == "n":
            break
    print("-----")
    print("Bye!")

blackjack()