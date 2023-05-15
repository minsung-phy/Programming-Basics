# 연습 5.3 덧셈만 가지고 제곱 계산하기 (for 루프 버전)

# while loop
def square(n):
    p = 0
    while not n == 0:
        n = abs(n)
        n, p = n-1, p+(n+n-1)
    return p

# for loop
def square(n):
    p = 0
    n = abs(n)
    for i in range(n,0,-1):
        p = p+(i+i-1)
    return p

# Test code
print(square(0))
print(square(1))
print(square(-2))
print(square(3))
print(square(-4))
print(square(5))
