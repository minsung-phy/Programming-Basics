# 실습 4.1 구간 수열의 합
def sumrange(m, n):
    if m <= n:
        return m + sumrange(m+1, n)
    else:
        return 0
    
def sumrange(m ,n):
    def loop(m, p):
        if m <= n:
            return loop(m+1, p+m)
        else:
            return p
    return loop(m, 0)

def sumrange(m ,n):
    p = 0
    while m <= n:
        m, p = m+1, p+m
    return p

# 실습 4.2 최대공약수 함수 완성
def gcd(m, n):
    while n != 0:
        m, n = n, m%n
    return m

# 실습 4.3 나눠 풀기 알고리즘 꼬리재귀 버전
def even(n):
    return n % 2 == 0

def odd(n):
    return n % 2 == 1

def gcd(m ,n):
    def loop(m ,n, p):
        if not (m == 0 or n == 0):
            if even(m) and even(n):
                return loop(m//2, n//2, p * 2)
            elif even(m) and odd(n):
                return loop(m//2, n, p)
            elif odd(m) and even(n):
                return loop(m, n//2, p)
            elif m <= n:
                return loop(m, (n-m)//2, p)
            else:
                return loop(n, (m-n)//2, p)
        else:
            if m == 0:
                return n * p
            else:
                return m * p
    return loop(m, n, 1)

# 실습 4.4 나눠 풀기 알고리즘 while 루프 버전
def gcd(m ,n):
    p = 1
    while not (m == 0 or n == 0):
        if even(m) and even(n):
            m ,n, p == m//2, n//2, p * 2
        elif even(m) and odd(n):
            m == m//2
        elif odd(m) and even(n):
            n == n//2
        elif m <= n:
            n == (n-m)//2
        else:
            m, n == n, (m-n)//2
    if m == 0:
        return n * p
    else:
        return m * p
    
# 실습 4.5 덧셈/뺄셈 알고리즘 : 꼬리재귀 함수 버전
def mult(m, n):
    def loop(n, k):
        if n > 0:
            return loop(n-1, m + k)
        else:
            return k
    return loop(n, 0)

# 실습 4.6 덧셈/뺄셈 알고리즘 : while 루프 버전
def mult(m, n):
    k = 0
    while n > 0:
        n, k = n-1, m + k
    return k

# 실습 4.7 덧셈/뺄셈/절반 알고리즘 : 재귀 함수 버전
def fastmult(m, n):
    if n > 0 and even(n):
        return fastmult(m+m, n//2)
    elif n > 0 and odd(n):
        return m + fastmult(m, n-1)
    else:
        return 0
    
# 실습 4.8 덧셈/뺄셈/절반 알고리즘 : 꼬리재귀 함수 버전
def fastmult(m, n):
    def loop(m, n, p):
        if n > 0 and even(n):
            return loop(m+m, n//2, p)
        elif n > 0 and odd(n):
            return loop(m, n-1, p+m)
        else:
            return p
    return loop(m, n, 0)

# 실습 4.9 덧셈/뺄셈/절반 알고리즘 : while 루프 버전
def fastmult(m, n):
    p = 0
    while n > 0:
        if even(n):
            m, n = m+m, n//2
        else:
            n, p = n-1, p+m
    return p 

# 실습 4.10 러시아 농부 알고리즘 : 재귀 함수 버전
def russian_mult(m, n):
    def loop(m, n):
        if n > 1:
            if even(n):
                return loop(m+m, n//2)
            else:
                return m + loop(m+m, n//2)
        else:
            return m
    if n > 0:
        return loop(m, n)
    else:
        return 0
    
# 실습 4.11 러시아 농부 알고리즘 : 꼬리재귀 함수 버전
def russian_mult(m, n):
    def loop(m, n, a):
        if n > 1:
            if even(n):
                return loop(m+m, n//2, a)
            else:
                return loop(m+m, n//2, a + m)
        else:
            return m + a
    if n > 0:
        return loop(m, n, 0)
    else:
        return 0
    
# 실습 4.12 러시아 농부 알고리즘 : while 루프 버전
def russian_mult(m, n):
    a = 0
    if n > 0:
        while n > 1:
            if even(n):
                m, n = m+m, n//2
            else:
                m, n, a = m+m, n//2, m + a
        return a + m 
    else:
        return 0
    
# 연습 4.1 카운트다운 타이머
from time import sleep
def countdown(n):
    if n > 0:
        print(n)
        sleep(1)
        countdown(n-1)
    else:
        print("Launch!")

def countdown(n):
    while n > 0:
        print(n)
        sleep(1)
        n = n-1
    print("Launch!")

def countdown2(n):
    if n > 0:
        if n > 9:
            print(n)
            sleep(1)
            countdown2(n-1)
        else:
            if n % 2 == 0:
                print("Launch Imminent!")
                sleep(1)
                countdown2(n-1)
            else:
                print(n)
                sleep(1)
                countdown2(n-1)
    else:
        print("Launch!")

def countdown2(n):
    while n > 0:
        if n > 9:
            print(n)
            sleep(1)
            n = n-1
        else:
            if n % 2 == 0:
                print("Launch Imminent!")
                sleep(1)
                n = n-1
            else:
                print(n)
                sleep(1)
                n = n-1
    print("Launch!")

# 연습 4.2 팩토리얼
def fac(n):
    if n > 1:
        return fac(n-1) * n
    else:
        return 1

def fac(n): 
    def loop(n, ans):
        if n > 1:
            return loop(n-1, ans*n)
        else:
            return ans
    return loop(n, 1)

def fac(n): 
    ans = 1
    while n > 1:
        n, ans = n-1, ans*n
    return ans

# 연습 4.3 삼각수
def trinum(n):
    if n > 0:
        return trinum(n-1) + n
    else:
        return 0
    
def trinum(n):
    def loop(n, p):
        if n > 0:
            return loop(n-1, p+n)
        else:
            return p
    return loop(n, 0)
    
def trinum(n):
    p = 0
    while n > 0:
        n, p = n-1, p+n
    return p

# 연습 4.4 덧셈만 가지고 제곱 계산하기
def square(n):
    if n != 0:
        n = abs(n)
        return (n+n-1) + square(n-1)
    else:
        return 0
    
def square(n):
    def loop(n, p):
        if n != 0:
            n = abs(n)
            return loop(n-1, n+n-1+p)
        else:
            return p
    return loop(n, 0)

def square(n):
    p = 0
    while n != 0:
        n = abs(n)
        n, p =n-1, n+n-1+p
    return p

# 연습 4.5 순열
def permutation(n, k):
    if k > 0:
        return (n-k+1) * permutation(n, k-1)
    else:
        return 1
    
def permutation(n, k):
    def loop(k, p):
        if k > 0:
            return loop(k-1, (n-k+1)*p)
        else:
            return p
    return loop(k, 1)
    
def permutation(n, k):
    p = 1
    while k > 0:
        k, p = k-1, (n-k+1)*p
    return p

# 연습 4.6 급수계산
def sum_of_num_over_next(n):
    if n > 0:
        return sum_of_num_over_next(n-1) + n/(n+1)
    else:
        return 0
    
def sum_of_num_over_next(n):
    def loop(n, p):
        if n > 0:
            return loop(n-1, p + n/(n+1))
        else:
            return p
    return loop(n, 0)

def sum_of_num_over_next(n):
    p = 0
    while n > 0:
        n, p = n-1, p + n/(n+1)
    return p

# 연습 4.7 정수 범위의 합
def add_range(start, stop, step):
    if start < stop:
        return start + add_range(start+step, stop, step)
    else:
        return 0
    
def add_range(start, stop, step):
    def loop(start, sum):
        if start < stop:
            return loop(start+step, sum + start)
        else:
            return sum
    return loop(start, 0)
    
def add_range(start, stop, step):
    sum = 0
    while start < stop:
        start, sum = start+step, sum + start
    return sum

# 연습 4.8 오늘부터 n일 뒤는 몇년 몇월 며칠?
def isleapyear(year):
    return year % 400 == 0 or year % 4 == 0 and year % 100 != 0

def next_month(year, month):
    if month == 12:
        year += 1
        month = 1
    else:
        month += 1
    return (year, month)

def days_in_month(year, month):
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        return 31
    elif month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    elif month == 2:
        if isleapyear(year):
            return 29
        else:
            return 28
        
def date_after_n_days(year, month, day, n):
    days_left = days_in_month(year,month) - day
    if days_left < n:
        n -= days_left
        (year, month) = next_month(year, month)
        days_this_month = days_in_month(year, month)
        while days_this_month < n:
            n -= days_this_month
            (year, month) = next_month(year, month)
            days_this_month = days_in_month(year,month)
        return (year, month, n)
    else:
        return (year, month, day + n)
    
# 4.9 자연수 수열의 합 : 나눠 풀기 알고리즘
def sigma2(n):
    if n > 0:
        if n % 2 == 0:
            return 2 * sigma2(n//2) + (n//2) * (n//2)
        else:
            return n + sigma2(n-1)
    else:
        return 0
    
def sigma2(n):
    def loop(n, m, acc):
        if n > 1:
            if n % 2 == 0:
                n = n//2
                return loop(n, m*2, acc+n*n*m)
            else:
                return loop(n-1, m, acc+n*m)
        else:
            return m + acc
    return loop(n,1,0)

def sigma2(n):
    m = 1
    acc = 0
    while n > 1:
        if n % 2 == 0:
            n //= 2
            acc += n * n * m
            m *= 2
        else:
            acc += n * m
            n -= 1
    return m + acc