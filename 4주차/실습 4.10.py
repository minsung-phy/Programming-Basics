def even(x):
    return x % 2 == 0

def russian_mult(m, n):
    def loop(m, n):
        if n > 1:
            if even(n):
                return loop(m+m, n//2)
            else:
                return m + loop(m+m, n//2)
        else: 
            return m
    if n > 0:
        return loop(m, n)
    else:
        return 0

print(russian_mult(57, 86))