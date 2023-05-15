# 실습 4.2

def gcd(m, n):
    while n != 0:
        m, n = n, m % n
    return m

print(gcd(18,48))