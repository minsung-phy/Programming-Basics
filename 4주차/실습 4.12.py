def russian_mult(m,n):
    if n > 0:
        a = 0
        while n > 1:
            if n % 2 == 1:
                m, n, a = m + m, n // 2, a + m
            else:
                m, n = m + m, n // 2
        return a + m
    else:
        return 0

print(russian_mult(57, 86))