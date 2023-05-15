# 연습 4.5 순열

# 재귀 함수
def permutation(n, k):
    if k > 0:
        return permutation(n, k-1) * (n -k +1)
    else:
        return 1

# 꼬리 재귀
def permutation(n, k):
    def loop(k, p):
        if k > 0:
            return loop(k-1, p * (n -k +1))
        else:
            return p
    return loop(k, 1)

# while loop
def permutation(n, k):
    p = 1
    while k > 0:
        k, p = k-1, p * (n -k +1)
    return p

# Test code
print(permutation(1,1)) # 1
print(permutation(2,1)) # 2
print(permutation(2,2)) # 2
print(permutation(3,1)) # 3
print(permutation(3,2)) # 6
print(permutation(3,3)) # 6
print(permutation(4,1)) # 4
print(permutation(4,2)) # 12
print(permutation(4,3)) # 24
print(permutation(4,4)) # 24
