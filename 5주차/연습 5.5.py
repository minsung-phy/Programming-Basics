# 연습 5.5 급수 계산 (for 루프 버전)

# while loop
def sum_of_num_over_next(n):
    p = 0
    while n>0:
        n,p = n-1, p + n/(n+1)
    return p

# for loop
def sum_of_num_over_next(n):
    p = 0
    for i in range(n,0,-1):
        p = p + i/(i+1)
    return p

# Test code
print(sum_of_num_over_next(0)) # 0
print(sum_of_num_over_next(1)) # 0.5
print(sum_of_num_over_next(3)) # 1.9166666...
print(sum_of_num_over_next(5)) # 3.5500000..
print(sum_of_num_over_next(10)) # 7.98012265..
print(sum_of_num_over_next(100)) # 95.80272149226131...

