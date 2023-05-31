import random
import time

# 수식 만들어보기 1
pi = 3.14
r = 5
area = pi * r ** 2
print(area)

# 수식 만들어보기 2
ca = 75
cb = 79
ai = 44
assignment = 5 * (ca + cb + ai)
print(assignment)

# 수식 만들어보기 3
lab = 5 + 7 + 8 + 7 + 8 + 7
print(lab)

# 변수와 함께 수식 만들어보기
pi = float(input("pi 값을 입력하세요: "))
r = float(input("반지름 값을 입력하세요: "))
area = pi * r ** 2
print(area)

# input 함수 사용해보기 1
x = input("변수를 입력하세요: ")
print("당신의 입력은", x, "입니다.")

# input 함수 사용해보기 2
y = int(input("2배할 숫자를 입력하세요: "))
print(y, "의 두배는", 2*y, "입니다.")

# 함수 만들기
def show_even_or_odd():
    num = int(input("정수를 입력하세요: "))
    if num % 2 == 0:
        print(num, ": 짝수입니다.")
    else:
        print(num, ": 홀수입니다.")

show_even_or_odd()

# 구구단 출력하기 - 기초
print(":: 구구단 3단 ::")
print("3 X 1 = 3")
print("3 X 2 = 6")
print("3 X 3 = 9")
print("3 X 4 = 12")
print("3 X 5 = 15")
print("3 X 6 = 18")
print("3 X 7 = 21")
print("3 X 8 = 24")
print("3 X 9 = 27")

# 구구단 출력하기 - for
print(":: 구구단 3단 ::")
for i in range(1,10):
    print("3 X", i, "=", 3*i)

# 구구단 출력하기 - input
print("구구단을 출력하는 프로그램입니다.")
n = int(input("몇단을 출력할까요? "))
print(":: 구구단", n, "단 ::")
for p in range(1,10):
    print(n, "X", p, "=", n*p)

# 구구단 출력하기 - 입력처리
print("구구단을 출력하는 프로그램입니다.")
def gugudan():
    n = input("몇단을 출력할까요? ")
    if n.isdigit():
        n = int(n)
        if 1 <= n <= 9:
            print(":: 구구단", n, "단 ::")
            for p in range(1,10):
                print(n, "X", p, "=", n*p)
        else:
            return gugudan()
    else:
        return gugudan()

# 구구단 출력하기 - 횟수제한
print("구구단을 출력하는 프로그램입니다.")
def gugudan():
    n = 0
    while True:
        x = input("몇단을 출력할까요? (1~9 사이의 정수) ")
        if x.isdigit():
            x = int(x)
            if 1<=x<=9:
                for i in range(1,10):
                    print(x, "X", i, "=", x*i)
                break
            else:
                n = n + 1
        else:
            n = n + 1
        if n > 4:
            print("잘못된 입력으로 프로그램을 종료합니다.")
            break

# 구구단 출력하기 - 맵시 
print("구구단을 출력하는 프로그램입니다.")
def gugudan():
    n = 0
    while True:
        x = input("몇단을 출력할까요? (1~9 사이의 정수) ")
        if x.isdigit():
            x = int(x)
            if 1<=x<=9:
                for i in range(1,10):
                    y = x*i
                    if y < 10:
                        print(x, "X", i, "= ", y)
                    else:
                        print(x, "X", i, "=", y)
                break
            else:
                n = n + 1
        else:
            n = n + 1
        if n > 4:
            print("잘못된 입력으로 프로그램을 종료합니다.")
            break

# 무작위 숫자 준비하기
a = random.randint(1, 9)
b = random.randint(1, 9)
print("첫째 숫자", a, ", 둘째 숫자", b)

# 무작위 구구단 준비하기
a = random.randint(1, 9)
b = random.randint(1, 9)
print(a, "X", b, "=", a * b)

# 무작위 구구단 물어보기
a = random.randint(1, 9)
b = random.randint(1, 9)
ans = int(input(str(a) + " X " + str(b) + " = "))
if ans == a * b:
    print("정답입니다!")
else:
    print("틀렸어요...")

# 시간 재기
def time_check(msg):
    start = time.perf_counter()
    value = input(msg + "\n >> ")
    end = time.perf_counter()
    print("당신이 문장을 입력하는데", round(end - start, 2), "초 걸렸습니다.")

time_check("apple")

# 무작위 구구단 시간재기
def gugudan():
    a = random.randint(1, 9)
    b = random.randint(1, 9)
    start = time.perf_counter()
    ans = int(input(str(a) + " X " + str(b) + " = "))
    end = time.perf_counter()
    delta_time = round(end-start, 2)
    if ans == a * b:
        print("정답입니다! (소요시간", delta_time, "초)")
    else:
        print("틀렸어요... (소요시간", delta_time, "초)")