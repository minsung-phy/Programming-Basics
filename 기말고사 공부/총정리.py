# 개념

# 1. 랜덤함수
import random

## 1. random.random() : 0.0 <= x < 1.0의 실수(float)를 반환 
x = random.random()
print(x) # 0.0 ~ 0.99999999...

## 2. random.uniform(a, b) : a <= x <= b의 실수(float)를 반환
x = random.uniform(10, 20)
print(x) # 10.00000 <= x <= 20.00000

## 3. randint(a, b) : a <= N <= b의 정수(int)를 반환, = randrange(a, b+1)
x = random.randint(10, 20)
print(x) # 10 <= x <= 20

## 4. randrange(a, b) : a <= x < b의 정수(int)를 반환
##    randrange(b) : 0 <= x < b의 정수(int)를 반환
x1 = random.randrange(10, 20)
print(x1) # 10 <= x < 20
x2 = random.randrange(20)
print(x2) # 0 <= x < 20

## 5. random.choice(seq)
## choice 함수는 매개변수로 seq 타입을 받는다. 시퀀스 데이터 타입은 문자열, 튜플, range, 리스트 타입들을 말한다.
## 시퀀스 함수는 인자로 받은 리스트, 튜플, 문자열, range에서 무작위로 하나의 원소를 뽑습니다.
## 만약 비어있는 시퀀스 타입의 객체를 인자로 넣는다면 (ex. 리스트가 비어있다면) indexerror의 예외가 발생한다. <indexerror: 시퀀스의 인덱스가 범위를 벗어났을때 발생하는 에러>
x1 = random.choice("BlockDMask")
print(x1) # "BlockDMask" 문자열 중 랜덤한 문자를 반환
try:
    x2 = random.choice("")
    print(x2) # indexerror 발생
except IndexError:
    print("IndexError")

## 6. random.sample(seq or set, N)
## 첫번째 매개 변수로 시퀀스 데이터 타입(튜플, 문자열, range, 리스트) 또는 set 타입(집합)을 받을 수 있다.
## 두번째 매개 변수로는 랜덤하게 뽑을 인자의 개수이다.
## sample 함수는 첫번째 인자로 받은 시퀀스데이터 or set에서 N개의 랜덤하고, unique(겹치지 않는 요소를 반환)하고, 순서상관없이 인자를 뽑아서 리스트로 만들어서 반환해준다.
## 두번째 매개 변수 N이 seq, set의 인자의 개수를 넘어갈때 valueError가 발생한다.
arr1 = "abc"
print(random.sample(arr1, 2)) # ['a','b'] or ['b','c'] or ['c','a'] 순서는 바뀔 수 있음
arr2 = "ccc"
try:
    print(random.sample(arr2, 10)) # ValueError 발생
except ValueError:
    print("ValueError")
arr3 = "ccc"
print(random.sample(arr3, 3)) # ['c','c','c'] 반환

## 7. random.shuffle(seq) : 데이터의 순서를 무작위로 랜덤하게 바꾸어 주는 함수
## 매개변수 x에는 시퀀스 데이터 타입이 들어가게 된다. 하지만 내부의 값을 무작위로 바꿔야 하기 때문에 내부 인자를 변경할 수 있는 리스트만 가능하게 된다. (문자열, 튜플 및 range(a,b)는 불가능)
## random.shuffle(리스트)의 반환은 없고, 인자로 들어온 리스트 내부의 데이터를 무작위로 섞습니다.
arr = [1,2,3,4,5,6,7,8,9,10]
print(arr) # [1,2,3,4,5,6,7,8,9,10]
random.shuffle(arr)
print(arr) # 무작위로 변경됨

# 2. 문자열 메소드
## s.strip(chars): 문자열 s의 양쪽 끝에서 문자열 chars에 있는 문자를 모두 제거하고 리턴한다. 인수가 비어있으면, 빈칸을 모두 제거하고 리턴한다.
## s.split(sep): 구분 문자열 sep을 중심으로 문자열 s를 분리하여 리스트로 모아 리턴한다. 인수가 비어있으면, 빈칸을 구분 문자열로 하여 분리한다.

# 3. 프린트 포맷
## 소수점 이하의 자리 수를 지정하여 프린트하고 싶으면 다음과 같이 포맷한다.
print("{0:.2f}".format(0.246)) # 0.25
print("{0:.1f}".format(0.246)) # 0.2

# 4. isdigit
# 문자열.isdigit(): 모든 문자가 숫자로만 이루어져있으면 True를 리턴하고, 문자가 하나라 있으면 False를 리턴한다. 음
#               음수나 소수는 -와 .때문에 문자로 취급한다.

# 5. continue
# continue는 예약어로서 프로그램의 실행 흐름을 바꾸는 명령이다.
# 루프의 코드 블록 실행 중 continue를 만나면, 감싸고 있는 루프의 남은 코드 블록을 실행하지 않고
# 루프의 시작 지점으로 돌아가서 실행을 재개한다.

# 6. 문자열 줄 맞추기 연산
# 문자열 메소드 / 실행 의미
# s.rjust(n) / n개의 빈자리를 확보한 다음, 문자열 s를 오른쪽 끝에 맞추는 메소드
# s.ljust(n) / n개의 빈자리를 확보한 다음, 문자열 s를 왼족 끝에 맞추는 메소





# 9주차
# 수식 만들어보기 1
area = 3.14 * 5 ** 2
print(area)

# 수식 만들어보기 2
CA = 75
CB = 79
AI = 44
assignment = 5 * (CA + CB + AI)
print(assignment)

# 수식 만들어보기 3
def floor(n):
    if n % 2 == 0:
        return 7
    else:
        return 8
lab = 5 + floor(2) + floor(3) + floor(4) + floor(5) + floor(6)
print(lab)

# 변수와 함께 수식 만들어보기
pi = 3.14
r = 5
area = pi * r ** 2
print(area)

# input 함수 사용해보기 1
a = input("입력하세요: ")
print("당신의 입력은", a, "입니다.")

# input 함수 사용해보기 2
a = int(input("정수를 입력하세요: "))
print(a, "의 두배는", 2*a, "입니다.")

# 함수 만들기
def show_even_or_odd():
    n = int(input("정수를 입력하세요: "))
    if n % 2 == 0:
        print(n, ": 짝수입니다.")
    else:
        print(n, ": 홀수입니다.")

# 구구단 출력하기 - 기초
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

# 구구단 출력하기 - for
print(":: 구구단 3단 ")
for i in range(1,10):
    print("3 x", i, "=", 3*i)

# 구구단 출력하기 - input
print("구구단을 출력하는 프로그램입니다.")
a = int(input("몇단을 출력할까요? "))
print(":: 구구단", a, "단 ::")
for i in range(1,10):
    print(a, "x", i, "=", a*i)

# 구구단 출력하기 - 입력처리
print("구구단을 출력하는 프로그램입니다.")
a = input("몇단을 출력할까요? ")
while not (a.isdigit() and 1<=int(a)<=9):
    a = input("몇단을 출력할까요?  (1~9 사이의 정수) ")
a = int(a)
print(":: 구구단", a, "단 ::")
for i in range(1,10):
    print(a, "x", i, "=", a*i)

# 구구단 출력하기 - 횟수제한
def gugudan():
    print("구구단을 출력하는 프로그램입니다.")
    a = input("몇단을 출력할까요? ")
    count = 0
    while not (a.isdigit() and 1<=int(a)<=9):
        a = input("몇단을 출력할까요?  (1~9 사이의 정수) ")
        count += 1
        if count > 4:
            print("잘못된 입력으로 프로그램을 종료합니다.")
            return
    a = int(a)
    print(":: 구구단", a, "단 ::")
    for i in range(1,10):
        print(a, "x", i, "=", a*i)

# 구구단 출력하기 - 맵시
def gugudan():
    print("구구단을 출력하는 프로그램입니다.")
    a = input("몇단을 출력할까요? ")
    count = 0
    while not (a.isdigit() and 1<=int(a)<=9):
        a = input("몇단을 출력할까요?  (1~9 사이의 정수) ")
        count += 1
        if count > 4:
            print("잘못된 입력으로 프로그램을 종료합니다.")
            return
    a = int(a)
    print(":: 구구단", a, "단 ::")
    for i in range(1,10):
        ans = a*i
        if ans < 10:
            print(a, "x", i, "= ", a*i)
        else:
            print(a, "x", i, "=", a*i)

# 무작위 숫자 준비하기
import random
a = random.randint(1,9)
b = random.randint(1,9)
print("첫째 숫자", a, ", 둘째숫자", b)

# 무작위 구구단 준비하기
a = random.randint(1,9)
b = random.randint(1,9)
print(a, "x", b, "=", a*b)

# 무작위 구구단 물어보기
a = random.randint(1,9)
b = random.randint(1,9)
ans = int(input(str(a) + " x " + str(b) + " = "))
if ans == a*b:
    print("정답입니다!")
else:
    print("틀렸어요...")


# 시간 재기
import time
def time_check(msg):
    start = time.perf_counter()
    value = input(msg + "\n >> ")
    end = time.perf_counter()
    print("당신이 문장을 입력하는데", round(end-start, 2), "초 걸렸습니다.")

# 무작위 구구단 시간재기
a = random.randint(1,9)
b = random.randint(1,9)
start = time.perf_counter()
ans = int(input(str(a) + " x " + str(b) + " = "))
end = time.perf_counter()
delta_time = round(end-start, 2)
if ans == a*b:
    print("정답입니다! (소요시간", delta_time, "초)")
else:
    print("틀렸어요...", delta_time, "초)")

# 무작위 구구단 완성하기
def gugudan():
    count = 0
    yes = 0
    start = time.perf_counter()
    while count < 5:
        a = random.randint(1,9)
        b = random.randint(1,9)
        ans = int(input(str(a) + " x " + str(b) + " = "))
        if ans == a*b:
            print("정답입니다!")
            yes += 1
        else:
            print("틀렸어요...")
        count += 1
    end = time.perf_counter()
    if yes == 5:
        print("축하합니다. 만점입니다!")
    elif yes == 0:
        print("모두 틀렸습니다 :(")
    else:
        print("5문제에서", yes, "개 맞췄습니다.")
    print("(총 소요시간", round(end-start, 2), "초)")

# 중첩 루프
# 실습 8.1 가로 변형
def digit_art_horizontal(n):
    for i in range(n):
        for j in range(n):
            print(j+1, end=' ')
        print()

def digit_art_horizontal_left_down(n):
    for i in range(n+1):
        for j in range(i):
            print(j+1, end=' ')
        print()

def digit_art_horizontal_left_up(n):
    for i in range(n):
        for j in range(n-i):
            print(j+1, end=' ')
        print()

# 실습 8.2 세로 변형
def digit_art_vertical(n):
    for i in range(n):
        for j in range(n):
            print(i+1, end=' ')
        print()

def digit_art_vertical_right_down(n):
    for i in range(n):
        print(" " * (n-i-1) * 2, end='')
        for j in range(i+1):
            print(i+1, end=' ')
        print()

# 실습 8.3 세로 방향 바꾸기
def digit_art_horizontal_alternate(n):
    for i in range(n):
        for j in range(n):
            if i % 2 == 0:
                print(j+1, end=' ')
            else:
                print(n-j, end=' ')
        print()

def digit_art_horizontal_vertical(n):
    for i in range(n):
        for j in range(n):
            if j % 2 == 0:
                print(i+1, end=' ')
            else:
                print(n-i, end=' ')
        print()

# 실습 8.4 버블정렬 구현
def bubblesort(ns):
    for k in range(len(ns)-1, 0, -1):
        for i in range(k):
            if ns[i] > ns[i+1]:
                ns[i], ns[i+1] = ns[i+1], ns[i]
    return ns

# 실습 8.5 기수정렬 구현
def radixsort(ds):
    if ds != []:
        length = len(ds[0])
        for i in range(length - 1, -1, -1):
            distributed = [[] for _ in range(10)]
            for d in ds:
                distributed[int(d[i])].append(d)
            ds = []
            for d in distributed:
                ds += d
        return ds
    else:
        return []

# 연습 8.1 구구단 출력
## 가. 가로전개 구구단
def gugudan_garo():
    for i in range(2,10):
        for j in range(2,10):
            ans = i*j            
            if j < 5:
                if ans < 10:
                    ans = str(ans)
                    ans = ans.ljust(2)
                    print(i, "x", j, "=", ans, end='   ')
                else:
                    print(i, "x", j, "=", ans, end='   ')
            elif j == 5:
                if ans < 10:
                    ans = str(ans)
                    ans = ans.ljust(2)
                    print(i, "x", j, "=", ans)
                else:
                    print(i, "x", j, "=", ans)
            elif 5< j < 9:
                if ans < 10:
                    ans = str(ans)
                    ans = ans.ljust(2)
                    print(i, "x", j, "=", ans, end='   ')
                else:
                    print(i, "x", j, "=", ans, end='   ')
            else:
                if ans < 10:
                    ans = str(ans)
                    ans = ans.ljust(2)
                    print(i, "x", j, "=", ans)
                else:
                    print(i, "x", j, "=", ans)

## 나. 세로전개 구구단
def gugudan_sero():
    for i in range(2,10):
        for j in range(2,6):
            ans = i*j
            ans = str(ans)
            ans = ans.ljust(2)
            print(j, "x", i, "=", ans, end='   ')
        print()
    for x in range(2,10):
        for y in range(6,10):
            ans = x*y
            ans = str(ans)
            ans = ans.ljust(2)
            print(y, "x", x, "=", ans, end='   ')
        print()

# 연습 8.2 ASCII Sharp 아트
def ascii_art(n):
    for i in range(n):
        for j in range(n):
            print("#", end=' ')
        print()

## 가. 십자가
def ascii_art_cross(n):
    for i in range(n):
        if i == (n//2):
            print("# " * n)
        else:
            print(" " * (n-2), "#", " " * (n-2))

def ascii_art_cross(n):
  for i in range(n):
    for j in range(n):
      if i == n // 2 or j == n // 2:
        print('#', end=' ')
      else:
        print(' ', end=' ')
    print()
    
# 나. 기울인 십자가
def ascii_art_X(n):
  for i in range(n):
    for j in range(n):
      if i == j or i + j == n - 1:
        print('#', end=' ')
      else:
        print(' ', end=' ')
    print()
            
# 다. 미음
def ascii_art_square(n):
    for i in range(n):
        for j in range(n):
            if  i == 0 or i == n - 1 or j == 0 or j == n-1:
                print("#", end=' ')
            else:
                print(" ", end=' ')
        print()

# 라. 마름모
def ascii_art_diamond(n):
    mid = n // 2
    for i in range(n):
        for j in range(n):
            if  abs(i-j) == mid or i+j == mid or i+j == n + mid - 1:
                print("#", end=' ')
            else:
                print(" ", end=' ')
        print()

# 연습 8.3 Number 아트
def numbers_art(n):
    for i in range(n):
        for j in range(n):
            print(j+1, end=' ')
        print()

# 가. 내리막
def numbers_art1(n):
    for i in range(n):
        for j in range(i+1):
            print(j+1, end=' ')
        print()

# 나. 줄타기
def numbers_art2(n):
    for i in range(n):
        print(" " * 2 * i, end='')
        for j in range(i,n):
            print(j+1, end=' ')
        print()

# 다. 오끄럼
def numbers_art3(n):
    for i in range(n):
        for j in range(n-i,n+1):
            print(j, end=' ')
        print()

# 라. 오르막
def numbers_art4(n):
    for i in range(n):
        print(" " * 2 * (n-i-1), end='')
        for j in range(n-i,n+1):
            print(j, end=' ')
        print()

# 연습 8.4 오른 뿔 그리기
def hornright(n):
    for i in range(1,n+1):
        k = i % 10
        for j in range(1,i+1):
            print(k,end=' ')
        print()
    for i in range(n-1,0,-1):
        k = i % 10
        for j in range(1,i+1):
            print(k,end=' ')
        print()

# 연습 8.5 로또 6/45
import random

def lotto645():
    list = []
    for j in range(6):
        a = random.randrange(1,46)
        while a in list:
            a = random.randrange(1,46)
        list.append(a)
        list.sort()
    for i in range(6):
        if list[i] < 10:
            print("0", list[i], sep='', end=' ')
        else:
            print(list[i], end=' ')

# 연습 8.6 중첩 리스트에서 원소 개수 세기
def count_deep(xss):
    counter = 0
    for xs in xss:
        if isinstance(xs, list):
            counter += count_deep(xs)
        else:
            counter += 1
    return counter

def count_the(x, xss):
    number = []
    counter = 0
    for xs in xss:
        if isinstance(xs, list):
            counter += count_the(x, xs)
        elif xs == x:
                counter += 1
    return counter



# 연습 9.1 희소 리스트 만들기
def sparse(ns):
    dic = {}
    index = 0
    for i in ns:
        index += 1
        if i != 0:
            dic[index-1] = i
    return dic

# 연습 9.2 두 희소 리스트 덧셈
def sparse_add(ms, ns):
    for key in ms:
        value = ns.get(key)
        if value != None:
            ms[key] += value
            del ns[key]
    for key in ns:
        ms[key] = ns[key]
    return ms













