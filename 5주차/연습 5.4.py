# 연습 5.4 순열 (for 루프 버전)

# while loop
def permutation(n, k):
    p = 1
    while k > 0:
        k, p = k-1, p * (n -k +1)
    return p

# for loop
def permutation(n, k):
    p = 1
    for i in range(k,0,-1):
        p =p * (n -i +1)
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
