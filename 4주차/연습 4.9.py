# 연습 4.9 자연수 수열의 합 : 나눠 풀기 알고리즘

# 재귀 함수
def sigma2(n):
    if n > 0:
        if n % 2 == 0:
            return 2 * sigma2(n//2) + (n//2) * (n//2)
        else:
            return n + sigma2(n-1)
    else:
        return 0

# 꼬리 재귀
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

# while loop
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


# Test code
print(sigma2(13))       # 91
print(sigma2(12))       # 78
print(sigma2(11))       # 66
print(sigma2(10))       # 55
print(sigma2(9))        # 45
print(sigma2(8))        # 36
print(sigma2(7))        # 28
print(sigma2(6))        # 21
print(sigma2(5))        # 15
print(sigma2(4))        # 10
print(sigma2(3))        # 6
print(sigma2(2))        # 3
print(sigma2(1))        # 1
print(sigma2(47733))    # 1139243511
print(sigma2(37387282)) # 698904446367403
