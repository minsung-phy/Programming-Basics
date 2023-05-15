# 카운트다운 타이머
from time import sleep
def countdown(n):
    for i in range(n, 0, -1):
        print(i)
        sleep(1)
    print("Launch!")

# 자연수 수열의 합 (순진무구 알고리즘)
def sigma(n):
    sum = 0
    for i in range(n, 0, -1):
        sum = sum + i        
    return sum

# 구간 수열의 합
def sumrange(m,n):
    sum = 0
    for i in range(m, n+1):
        sum = sum + i
    return sum

# 팩토리얼
def fac(n):
    ans = 1
    for i in range(n, 1, -1):
        ans = ans * i
    return ans

# 거듭제곱 (순진무구 알고리즘)
def power(b,n):
    prod = 1
    for i in range(n, 0, -1):
        prod = b * prod
    return prod
