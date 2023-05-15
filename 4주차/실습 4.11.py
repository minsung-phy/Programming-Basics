def even(x):
    return x % 2 == 0

def russian_mult(m, n):
    def loop(m, n, a):
        if n > 1:
            if even(n):
                return loop(m+m, n//2, a)
            else:
                return loop(m+m, n//2, m + a)
        else: 
            return a + m 
    if n > 0:
        return loop(m, n, 0)
    else:
        return 0

print(russian_mult(57, 86))