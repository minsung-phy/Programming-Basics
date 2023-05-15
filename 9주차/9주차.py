## 수식 만들어보기 1
# 원의 면적을 구하는 식은 pi * r^2 입니다.
# pi의 값이 3.14, 원의 반지름 r의 값이 5일때, 원의 면적을 구하는 수식을 완성하세요.

pi = 3.14
r = 5
area = pi * r ** 2

print(area)

## 수식 만들어보기 2
# 2023년도 봄학기 프로그래밍기초는 3개의 반이 있습니다.
# CA반의 수강생은 75명, CB반의 수강생은 79명, AI반의 수강생은 44명입니다.
# 한학기 동안 과제가 총 5번 있었고, 모든 학생이 과제를 제출했다면, 체점해야할 제출물의 수는 모두 얼마일까요?

CA = 75
CB = 79
AI = 44
assignment = 5 * (CA + CB + AI)

print(assignment)

## 수식 만들어보기 3
# H대학 E캠퍼스 N공학관 건물의 각 층에는 연구실이 있습니다.
# 1층에는 5개의 연구실이 있고, 그 외에 홀수 층에는 8개, 짝수 층에는 7개의 연구실이 있습니다.
# 건물이 총 6층까지 있을 때, 연구실은 총 몇 개일까요?

lab = 5 + 7 + 8 + 7 + 8 + 7

print(lab)

## 변수와 함께 수식 만들어보기
# 원의 면적을 구하는 식은 pi * r^2 입니다.
# pi의 값을 변수 pi, 원의 반지름 r의 값을 변수 r에 저장했을때, 원의 면적을 구하는 수식을 완성하세요.

pi2 = input("pi: ")
r2 = input("r: ")
area2 = float(pi2) * int(r2) ** 2

print(area2)

## input 함수 사용해보기 1
# 사용자의 입력을 받아서 변수에 저장한 다음, 화면에 다음과 같은 방식으로 출력해주는 코드를 작성하세요. (아래 예시에서 abc는 사용자의 입력입니다.)
# 당신의 입력은 abc입니다.

inp = input("입력: ")
print("당신의 입력은", inp, "입니다.")

## input 함수 사용해보기 2
# 사용자의 입력을 받아서 정수값으로 바꿔 변수에 저장한 다음, 그 값의 두배를 다음과 같은 방식으로 출력해주는 코드를 작성하세요. 
# (아래 예시에서 3은 사용자의 입력입니다.)
# 3의 두배는 6입니다.

inp2 = input("입력: ")
ans = 2 * int(inp2)
print(inp2, "의 두배는", ans, "입니다.")

## 함수 만들기
# 사용자의 입력을 받아서 정수값으로 바꿔 변수에 저장한 다음, 그 값이 짝수인지 홀수인지를 출력해주는 함수 show_even_or_odd을 작성하세요
# 정수를 입력하세요 : 3
# 3 : 홀수입니다.
# 정수를 입력하세요 : 2
# 2 : 짝수입니다.

inp = int(input("정수를 입력하세요 : "))
def show_even_or_odd():
    if inp % 2 == 0:
        print(inp, " : 짝수입니다.")
    else:
        print(inp, " : 홀수입니다.")

show_even_or_odd()

## 구구단 출력하기 - 기초
# 다음과 같이 구구단 3단을 출력하는 코드를 작성하세요.
# print 함수 10번을 사용해야 합니다.

print(":: 구구단 3단 ::")
print("3 x 1 = 3")
print("3 x 2 = 6")
print("3 x 3 = 9")
print("3 x 4 = 12")
print("3 x 5 = 15")
print("3 x 6 = 18")
print("3 x 7 = 21")
print("3 x 8 = 24")
print("3 x 9 = 27")

## 구구단 출력하기 - for
# 다음과 같이 구구단 3단을 출력하는 코드를 작성하세요.
# print 함수를 2번, for 구문을 한번 사용해야 합니다.

print(":: 구구단 3단 ::")
for n in range(1,10):
    print("3 x", n, "=", 3 * n)

## 구구단 출력하기 - input
# 사용자에게 1~9 사이의 정수 값 n을 입력 받아 구구단 n단을 출력하는 코드를 작성하세요.

print("구구단을 출력하는 프로그램입니다.")
n = int(input("몇단을 출력할까요? "))
print(":: 구구단", n, "단 ::")
for p in range(1,10):
    print(n, "x", p, "=", n * p)

## 구구단 출력하기 - 입력처리
# 사용자에게 1~9 사이의 정수 값 n을 입력 받아 구구단 n단을 출력하는 코드를 작성하세요.
# 사용자의 입력이 1~9 사이의 정수 값이 아닐 경우, 다시 입력받아야 합니다.

print("구구단을 출력하는 프로그램입니다.")

def gugudan():
    i = input("몇단을 출력할까요? ")
    if i.isdigit():
        j = int(i)
        if 1 <= j < 10:
            print(":: 구구단", j, "단 ::")
            for k in range(1,10):
                print(j, "x", k, "=", j * k)
        else:
            return gugudan()
    else:
        return gugudan()

gugudan()

## 구구단 출력하기 - 횟수제한
# 사용자에게 1~9 사이의 정수 값 n을 입력 받아 구구단 n단을 출력하는 코드를 작성하세요.
# 사용자의 입력이 1~9 사이의 정수 값이 아닐 경우, 다시 입력받아야 합니다.
# 만약 사용자가 5회 이상 잘못된 입력을 할 경우, 적절한 메시지와 함께 프로그램을 종료합니다.

print("구구단을 출력하는 프로그램입니다.")

def gugudan():
    count = 0
    while True:
        i = input("몇단을 출력할까요? (1~9 사이의 정수)")
        if i.isdigit():
            j = int(i)
            if 1 <= j < 10:
                print(":: 구구단", j, "단 ::")
                for k in range(1,10):
                    print(j, "x", k, "=", j * k)
                break
            else:
                count = count + 1
        else:
            count = count + 1

        if count >= 5:
            print("잘못된 입력으로 프로그램을 종료합니다.")
            break

gugudan()
           
## 구구단 출력하기 - 맵시
# 앞서 작성한 구구단 프로그램을 출력할 때, 다음과 같이 우측 정렬로 출력하도록 수정하시오.
# 힌트: 결과 값이 10 이상인 경우와 그렇지 않은 경우로 나눠서 생각해보세요.

print("구구단을 출력하는 프로그램입니다.")

def gugudan():
    count = 0
    while True:
        i = input("몇단을 출력할까요? (1~9 사이의 정수) ")
        if i.isdigit():
            j = int(i)
            if 1 <= j < 10:
                print(":: 구구단", j, "단 ::")
                for k in range(1,10):
                    ans = j * k
                    if ans < 10:
                        print(j, "x", k, "= ", j * k)
                    else:
                        print(j, "x", k, "=", j * k)
                break
            else:
                count = count + 1
        else:
            count = count + 1

        if count >= 5:
            print("잘못된 입력으로 프로그램을 종료합니다.")
            break

gugudan()

## 무작위 숫자 준비하기
# 무작위로 1~9 사이의 숫자 두개를 생성하여 다음과 같이 출력하는 코드를 작성하세요. 
# 첫째 숫자 1, 둘째 숫자 3
# random 모듈의 randint 함수를 사용합니다.
# import random
# random.randint(1, 9)

import random
print("첫째 숫자", random.randint(1, 9), ", 둘째 숫자", random.randint(1, 9))

## 무작위 구구단 준비하기
# 무작위로 1~9 사이의 숫자 두개를 생성하여 다음과 같이 구구단을 출력하는 코드를 작성하세요.
# 3 x 3 = 9
# 8 x 7 = 56
# 3 x 9 = 27

import random

a = random.randint(1, 9)
b = random.randint(1, 9)
c = random.randint(1, 9)
d = random.randint(1, 9)
e = random.randint(1, 9)
f = random.randint(1, 9)

print(a, "x", b, "=", a*b)
print(c, "x", d, "=", c*d)
print(e, "x", f, "=", e*f)

## 무작위 구구단 물어보기
# 무작위로 1~9 사이의 숫자 두개를 생성하여 구구단을 물어보고, 사용자의 답을 입력받아 결과를 알려주는 프로그램을 작성하세요.
# 3 x 9 = 27
# 정답입니다!
# 7 x 5 = 27
# 틀렸어요...

import random

a = random.randint(1, 9)
b = random.randint(1, 9)
mul = int(input(str(a) + " x " + str(b) + " = "))
if mul == a * b: 
    print("정답입니다!")
else:
    print("틀렸어요...")

## 시간 재기
# 사용자가 제시한 문자를 입력하는데 걸린 시간을 측정하는 수를 작성해서 실행해보세요.

import time
def time_check(msg):
    start = time.perf_counter()
    value = input(msg + "\n >> ")
    end = time.perf_counter()
    print("당신이 문장을 입력하는데", round(end-start, 2), "초 걸렸습니다.")

time_check("yummy")

## 무작위 구구단 시간재기
# 무작위로 1~9 사이의 숫자 두개를 생성하여 구구단을 물어보고, 
# 사용자의 답을 입력받아 결과와 함께 맞추는데 걸린 시간을 알려주는 프로그램을 작성하시오.

import time
import random

def time_gugu():
    a = random.randint(1, 9)
    b = random.randint(1, 9)
    start = time.perf_counter()
    mul = int(input(str(a) + " x " + str(b) + " = "))
    end = time.perf_counter()
    if mul == a * b: 
        print("정답입니다! (소요시간", round(end-start, 2), "초)")
    else:
        print("틀렸어요... (소요시간", round(end-start, 2), "초)")

time_gugu()