# 재귀 함수
def trinum(n):
    if n > 0:
        return trinum(n-1) + n
    else: 
        return 0

# 꼬리재귀 함수
def trinum_t(n):
    def loop(n, p):
        if n > 0:
            return loop(n-1, p+n) 
        else: 
            return p
    return loop(n, 0)

# while 루프
def trinum_w(n):
    p = 0
    while n > 0:
        n, p = n-1, p+n
    return p

# Test code 재귀 함수
print(trinum(1))  # 1
print(trinum(3))  # 6
print(trinum(6))  # 21
print(trinum(11)) # 66
print(trinum(0))  # 0
print(trinum(-3)) # 0

# Test code 꼬리재귀 함수
print(trinum_t(1))  # 1
print(trinum_t(3))  # 6
print(trinum_t(6))  # 21
print(trinum_t(11)) # 66
print(trinum_t(0))  # 0
print(trinum_t(-3)) # 0

# Test code while 루프
print(trinum_w(1))  # 1
print(trinum_w(3))  # 6
print(trinum_w(6))  # 21
print(trinum_w(11)) # 66
print(trinum_w(0))  # 0
print(trinum_w(-3)) # 0