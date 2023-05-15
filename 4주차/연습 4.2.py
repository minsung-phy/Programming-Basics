# 연습 4.2 팩토리얼

# 재귀 함수
def fac(n):
    if n > 1:
        return fac(n-1) * n
    else:
        return 1

# 꼬리 재귀
def fac(n):
    def loop(n, ans):
        if n > 1:
            return loop(n-1, ans * n)
        else:
            return ans
    return loop(n,1)

# while loop
def fac(n):
    ans= 1
    while n > 1:
        n, ans =n-1, ans * n
    return ans
