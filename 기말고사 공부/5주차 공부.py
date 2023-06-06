# 실습 5.1 for 루프 작성 연습
from time import sleep
def countdown(n):
    while n > 0:
        print(n)
        sleep(1)
        n = n-1
    print("Launch!")

def countdown(n):
    for i in range(n,0,-1):
        print(i)
        sleep(1)
    print("Launch!")

def sigma(n):
    sum = 0
    while n > 0:
        n, sum = n-1, n+sum
    return sum

def sigma(n):
    sum = 0
    for i in range(n,0,-1):
        sum += i
    return sum

def sumrange(m,n):
    sum = 0
    while m <= n:
        sum = sum + m
        m = m + 1
    return sum

def sumrange(m,n):
    sum = 0
    for i in range(m,n+1):
        sum = sum + i
    return sum

def fac(n):
    ans = 1
    while n > 0:
        n, ans = n-1, ans*n
    return ans

def fac(n):
    ans = 1
    for i in range(n,0,-1):
        ans = ans*i
    return ans

def power(b, n):
    prod = 1
    while n > 0:
        prod = b * prod
        n = n - 1
    return prod

def power2(b, n):
    prod = 1
    for i in range(n,0,-1):
        prod = b * prod
    return prod

# 실습 5.2 insert: 재귀 함수 버전
def insert(x, ss):
    if ss != []:
        if x <= ss[0]:
            return [x] + ss
        else:
            return [ss[0]] + insert(x,ss[1:])
    else:
        return [x]
    
# 실습 5.3 insert: 꼬리재귀 함수 버전
def insert(x, ss):
    def loop(ss, left):
        if ss != []:
            if x <= ss[0]:
                left.append(x)
                return left + ss
            else:
                left.append(ss[0])
                return left + loop(ss[1:], left)
        else:
            left.append(x)
            return left
    return loop(ss, [])


def insert(x, ss):
    def loop(ss, left):
        if ss != []:
            if x <= ss[0]:
                left.append(x)
                return left + ss
            else:
                left.append(ss[0])
                return loop(ss[1:], left)
        else:
            left.append(x)
            return left
    return loop(ss, [])
    
# 실습 5.4 insert : while 루프 버전
def insert(x, ss):
    left = []
    while ss != []:
        if x <= ss[0]:
            left.append(x)
            return left + ss
        else:
            left.append(ss[0])
            ss = ss[1:]
    left.append(x)
    return left
    
# 실습 5.5 insert_sort : 꼬리재귀 함수 버전
def insertion_sort(xs):
    if xs != []:
        return insert(xs[0], insertion_sort(xs[1:]))
    else:
        return []
    
def insertion_sort(xs):
    def loop(xs, ss):
        if xs != []:
            return loop(xs[1:], insert(xs[0],ss))
        else:
            return ss
    return loop(xs,[])

# 실습 5.6 insert_sort : while 루프 버전
def insertion_sort(xs):
    ss = []
    while xs != []:
        xs, ss = xs[1:], insert(xs[0],ss)
    return ss

# 실습 5.7 insert_sort : for 루프 버전
def insertion_sort(xs):
    ss = []
    for i in xs:
        ss = insert(i,ss)
    return ss

# 실습 5.8 merge : 꼬리재귀 함수 버전
def merge(left, right):
    if not (left == [] or right == []):
        if left[0] <= right[0]:
            return [left[0]] + merge(left[1:], right)
        else:
            return [right[0]] + merge(left, right[1:])
    else:
        return left + right
    
def merge(left, right):
    def loop(left, right, ss):
        if not (left == [] or right == []):
            if left[0] <= right[0]:
                ss.append(left[0])
                return loop(left[1:], right, ss)
            else:
                ss.append(right[0])
                return loop(left, right[1:], ss)
        else:
            return ss + left + right
    return loop(left, right, [])

# 실습 5.9 merge : while 루프 버전
def merge(left, right):
    ss = []
    while not (left == [] or right == []):
        if left[0] <= right[0]:
            ss.append(left[0])
            left = left[1:]
        else:
            ss.append(right[0])
            right = right[1:]
    else:
        return ss + left + right

# 실습 5.10 partition : 꼬리재귀 함수 버전
def partition(pivot, xs):
    if xs != []:
        left, right = partition(pivot, xs[1:])
        if xs[0] <= pivot:
            left.append(xs[0])
        else:
            right.append(xs[0])
        return left, right
    else:
        return [], []
    
def partition(pivot, xs):
    def loop(xs, left, right):
        if xs != []:
            if xs[0] <= pivot:
                left.append(xs[0])
            else:
                right.append(xs[0])
            return loop(xs[1:], left, right)
        else:
            return left, right
    return loop(xs,[],[])

# 실습 5.11 partition : while 루프 버전
def partition(pivot, xs):
    left, right = [], []
    while xs != []:
        if xs[0] <= pivot:
            left.append(xs[0])
        else:
            right.append(xs[0])
        xs = xs[1:]
    return left, right

# 실습 5.12 partition : for 루프 버전
def partition(pivot, xs):
    left, right = [], []
    for i in xs:
        if i <= pivot:
            left.append(i)
        else:
            right.append(i)
    return left, right

# 연습 5.1 팰린드롬 검사 함수
def ispalindrome(s):
    if len(s) <= 1:
        return True
    elif s[0] != s[-1]:
        return False
    else:
        return ispalindrome(s[1:-1])
    
def ispalindrome(s):
    return len(s) <= 1 or s[0] == s[-1] and ispalindrome(s[1:-1])

# 연습 5.2 삼각수 for 루프 버전
def trinum(n):
    p = 0
    for i in range(n,0,-1):
        p = p+i
    return p

# 연습 5.3 덧셈만 가지고 제곱 계산하기 for 루프 버전
def square(n):
    p = 0
    n = abs(n)
    for i in range(n,0,-1):
        p = p + (i+i-1)
    return p

# 연습 5.4 순열 for 루프 버전
def permutation(n, k):
    p = 1
    for i in range(k,0,-1):
        p = p * (n -i +1)
    return p

# 연습 5.5 급수 계산 for 루프 버전
def sum_of_num_over_next(n):
    p = 0
    for i in range(n,0,-1):
        p = p + i/(i+1)
    return p
  
# 연습 5.6 윤년 출력 프로시저
def is_leap_year(year):
    return year % 400 == 0 or year % 4 == 0 and year % 100 != 0

def print_leap_year(yearfrom, yearto):
    print("Leap years between", yearfrom, "and", yearto, ":")
    for i in range(yearfrom, yearto+1):
        if is_leap_year(i) == True:
            print(i)

# 연습 5.7 ISBN-10 코드 검증
def isbn10(s):
    total = 0
    for i in range(1,10):
        total = total + int(s[i-1]) * i
    last = total % 11
    if last == 10:
        return s[9] == "X"
    else:
        return s[9] == str(last)
    
# 연습 5.10 재귀 함수를 꼬리재귀, while 루프, for 루프 함수로 변환하기
def updown(ns):
    if ns != []:
        if ns[0] % 2 == 0:
            return [ns[0]//2] + updown(ns[1:])
        else:
            return [ns[0]*2] + updown(ns[1:])
    else:
        return []    
    
def updown(ns):
    def loop(ns, p):
        if ns != []:
            if ns[0] % 2 == 0:
                return loop(ns[1:], p + [ns[0]//2])
            else:
                return loop(ns[1:], p + [ns[0]*2])
        else:
            return p  
    return loop(ns, [])

def updown(ns):
    p = []
    while ns != []:
        if ns[0] % 2 == 0:
            ns, p = ns[1:], p + [ns[0]//2]
        else:
            ns, p = ns[1:], p + [ns[0]*2]
    return p  
    
def updown(ns):
    p = []
    for i in ns:
        if i % 2 == 0:
            p = p + [i//2]
        else:
            p = p + [i*2]
    return p  

print(updown([4,6,5,3,7,6,2,1,3,2]))
# [2,3,10,6,14,3,1,2,6,1]