# 연습 4.4 덧셈만 가지고 제곱 계산하기

# 재귀 함수
def square(n):
    if not n == 0:
        n = abs(n)
        return (n+n-1) + square(n-1)
    else:
        return 0

# 꼬리 재귀
def square(n):
    def loop(n, p):
        if not n == 0:
            n = abs(n)
            return loop(n-1, p+(n+n-1))
        else:
            return p
    return loop(n,0)

# while loop
def square(n):
    p = 0
    while not n == 0:
        n = abs(n)
        n, p = n-1, p+(n+n-1)
    return p


# Test code
print(square(0))
print(square(1))
print(square(-2))
print(square(3))
print(square(-4))
print(square(5))

