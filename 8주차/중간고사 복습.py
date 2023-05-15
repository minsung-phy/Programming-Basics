#################################################################
#
# 2023년
# 프로그래밍기초 Programming Fundamentals
# 중간고사 뼈대코드 Midterm. Skeleton Code
#
#################################################################
#
# 학번(student id) :
# 이름(name) :
#
#################################################################
# 1. log2(n) 어림잡아 구하기
#################################################################

def log2r(n):
    if n >= 2:
        return 1 + log2r(n // 2)
    else:
        return 0

def log2t(n):
    def loop(n, p):
        if n >= 2:
            return loop(n // 2, p + 1)
        else:
            return p
    return loop(n,0)

def log2w(n):
    p = 0
    while n >= 2:
        n, p = n // 2, p + 1
    return p

#################################################################
# 2. 가위바위보 게임 처리기
#################################################################
#
# "R" means 'rock' 바위
# "S" means 'scissors' 가위
# "P" means 'paper' 보
#

#######
# 2.1
def eval(you, com):
    if you + com in ["RS","SP", "PR"]:
        return 1
    elif you == com:
        return 0
    else:
        return -1

#######
# 2.2
def wins_r(game_list):
    if game_list != []:
        if eval(game_list[0][0],game_list[0][1]) == 1:
            return 1 + wins_r(game_list[1:])
        else:
            return wins_r(game_list[1:])
    else:
        return 0
    

#######
# 2.3
def wins_t(game_list):
    def loop(game_list, p):
        if game_list != []:
            if eval(game_list[0][0],game_list[0][1]) == 1:
                return loop(game_list[1:], p + 1)
            else:
                return loop(game_list[1:], p)
        else:
            return p
    return loop(game_list, 0)

#######
# 2.4
def wins_w(game_list):
    p = 0
    while game_list != []:
        if eval(game_list[0][0],game_list[0][1]) == 1:
            game_list, p = game_list[1:], p + 1
        else:
            game_list = game_list[1:]
    return p
 

#######
# 2.5
wins_for_version_is_possible = True
def wins_f(game_list):
    p = 0
    for i in game_list:
        if eval(i[0],i[1]) == 1:
            p = p + 1
    return p


#################################################################
# 3. 모스 부호
#################################################################
#
# 1 : . - - - -
# 2 : . . - - -
# 3 : . . . - -
# 4 : . . . . -
# 5 : . . . . .
# 6 : - . . . .
# 7 : - - . . .
# 8 : - - - . .
# 9 : - - - - .
# 0 : - - - - -

#######
# 3.1
def digit2morse(d):
    if d < 6:
        return "." * d + "-" * (5-d)
    else:
        return "-" * (d-5) + "." * (10-d)


#######
# 3.2
def is_digit_morse(m):
    digit_morse = [".----", "..---", "...--", "....-", ".....", "-....", "--...", "---..", "----.", "-----"]
    if m.strip() in digit_morse:
        return True
    else:
        return False
    
#######
# 3.3
def morse2digit(m):
    digit_morse = ["-----",".----", "..---", "...--", "....-", ".....", "-....", "--...", "---..", "----."]
    if m.strip() in digit_morse:
        numOfDot = m.count(".")
        if m[0] == ".":
            return numOfDot
        elif numOfDot == 0:
            return 0
        else:
            return 10 - numOfDot
    else:
        return None

#######
# 3.4
def moerse2number(m):
    if m == "" : 
        return -1
    value = ""
    while m != "":
        m = m.strip()
        v, _, m = m.partition(" ")
        if is_digit_morse(v):
            value = value + str(morse2digit(v))
        else:
            return -1
    return int(value)


###############################################################
# 아래 채점 코드를 지우거나 수정하지 마세요.
# do not remove or modify below code.
###############################################################

def to_str(s):
    return "'" + s + "'"

# checker1 for testing log2r, log2t, log2w
def checker1s(msg, log_func):
    import random
    import math
    point = 0
    tries = 5
    for n in random.sample(range(10000), tries):
        test_value = n
        answer = int(math.log(test_value, 2))
        your_value = log_func(test_value)
        if your_value == answer:
            point += 1
        else:
            print(msg + "(",test_value,") =",answer,", your answer is",your_value)
    print(msg, ":", point, "/", tries)

def checker1():
    checker1s("[1.1] log2r", log2r)
    checker1s("[1.2] log2t", log2t)
    checker1s("[1.3] log2w", log2w)

# checker2 for testing eval, wins_r, wins_t, wins_t, and optionally wins_f
def checker2e(msg, verbose):
    import random
    import math
    point = 0
    all_cases = [ (("R", "R"), 0), (("R", "S"), 1), (("R", "P"), -1),
                  (("S", "R"), -1), (("S", "S"), 0), (("S", "P"), 1),
                  (("P", "R"), 1), (("P", "S"), -1), (("P", "P"), 0), ]
    tries = len(all_cases)
    for (you, com), answer in all_cases:
        your_value = eval(you, com)
        if your_value == answer:
            point += 1
        else:
            if verbose:
                print(msg + "("+to_str(you)+", "+to_str(com)+") =",answer,", your answer is",your_value)
    if verbose:
        print(msg, ":", point, "/", tries)
    else:
        return point

checker2_cases = [
    ([('R', 'R'), ('R', 'S'), ('P', 'P'), ('P', 'S'), ('R', 'R'), ('R', 'P'), ('S', 'P'), ('R', 'R'), ('S', 'P')], 3),
    ([], 0),
    ([('P', 'S'), ('P', 'R')], 1),
    ([('P', 'P'), ('R', 'R'), ('P', 'R'), ('P', 'S'), ('P', 'R'), ('S', 'S')], 2),
    ([('P', 'S'), ('R', 'P'), ('P', 'S'), ('R', 'S'), ('P', 'R'), ('P', 'R'), ('S', 'P'), ('S', 'R')], 4),
    ([('R', 'R'), ('S', 'R'), ('R', 'R'), ('P', 'P'), ('P', 'R'), ('P', 'R'), ('S', 'S'), ('R', 'R'), ('S', 'P'), ('R', 'P')], 3),
    ([('S', 'R'), ('P', 'R')], 1),
    ([('S', 'P'), ('P', 'P'), ('S', 'R')], 1),
    ([('R', 'P'), ('P', 'P'), ('P', 'P')], 0) ]

def checker2w(msg, win_func):
    if checker2e("", False) == 9:
        tries = len(checker2_cases)
        point = 0
        for game_data, answer in checker2_cases:
            your_value = win_func(game_data[:])
            if your_value == answer:
                point += 1
            else:
                print(msg + "(",game_data,") =",answer,", your answer is",your_value)
        print(msg, ":", point, "/", tries)
    else:
        print(msg, ": eval function has problem")

def checker2():
    checker2e("[2.1] eval", True)
    checker2w("[2.2] wins_r", wins_r)
    checker2w("[2.3] wins_t", wins_t)
    checker2w("[2.4] wins_w", wins_w)
    if wins_for_version_is_possible == True:
        checker2w("[2.5] wins_f", wins_f)

# checker3 for testing digit2morse, is_digit_morse, morse2digit and, morse2number

checker3_cases = [("...--", 3), ("-----", 0), (".....", 5), ("...-", None)]

def checker3dm(msg):
    tries = len(checker3_cases)
    point = 0
    for m, d in checker3_cases:
        if d != None:
            your_value = digit2morse(d)
            if your_value == m:
                point += 1
            else:
                print(msg + "(",d,") =",to_str(m),", your answer is",your_value)
        else:
            tries = tries - 1
    print(msg, ":", point, "/", tries)

def checker3md(msg):
    tries = len(checker3_cases)
    point = 0
    for m, d in checker3_cases:
        your_value = morse2digit(m)
        if your_value == d:
            point += 1
        else:
            print(msg + "(",to_str(m),") =",d,", your answer is",your_value)
    print(msg, ":", point, "/", tries)

checker3_cases_2nd = [
    (".----", True),
    ("... -", False),
    (".....", True),
    ("-....", True),
    ("-...", False),
]

def checker3if(msg):
    tries = len(checker3_cases_2nd)
    point = 0
    for m, answer in checker3_cases_2nd:
        your_value = is_digit_morse(m)
        if your_value == answer:
            point += 1
        else:
            print(msg + "(",to_str(m),") =",answer,", your answer is",your_value)
    print(msg, ":", point, "/", tries)

checker3_cases_3rd = [
    ("-----", 0),
    ("...-- -----", 30),
    ("..--- -----    ..---  ...--", 2023),
    ("----.                     ----.", 99),
    ("----- ---", -1),
    ("...-- - ----", -1),
    ("", -1),
]

def checker3mn(msg):
    tries = len(checker3_cases_3rd)
    point = 0
    for m, answer in checker3_cases_3rd:
        your_value = morse2number(m)
        if your_value == answer:
            point += 1
        else:
            print(msg + "(",to_str(m),") =",answer,", your answer is",your_value)
    print(msg, ":", point, "/", tries)


def checker3():
    checker3dm("[3.1] digit2morse")
    checker3if("[3.2] is_digit_morse")
    checker3md("[3.3] morse2digit")
    checker3mn("[3.4] morse2number")


def check_all():
    checker1()
    checker2()
    checker3()

check_all()