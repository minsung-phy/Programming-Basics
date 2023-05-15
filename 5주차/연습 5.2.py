# 연습 5.2 삼각수 (for 루프 버전)

# while 루프
def trinum(n):
    p = 0
    while n > 0:
        n, p = n-1, p+n
    return p

# for 루프
def trinum(n):
    p = 0
    for i in range(n,0,-1):
        p= p+i
    return p

# Test code
print(trinum(1))  # 1
print(trinum(3))  # 6
print(trinum(6))  # 21
print(trinum(11)) # 66
print(trinum(0))  # 0
print(trinum(-3)) # 0
