# 실습 4.6

def mult(m, n):
    ans = 0
    while n > 0:
         n, ans = n - 1, m + ans
    return ans

print(mult(3, 6))