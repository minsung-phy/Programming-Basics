# 실습 4.5

def mult(m, n):
    def loop(n, ans):
        if n > 0:
            return loop(n-1, m+ans)
        else:
            return ans
    return loop(n, 0)

print(mult(3, 6))