# 연습 4.6 급수 계산

# 재귀 함수
def sum_of_num_over_next(n):
    if n>0:
        return sum_of_num_over_next(n-1) + (n/(n+1))
    else:
        return 0

# 꼬리 재귀
def sum_of_num_over_next(n):
    def loop(n,p):
        if n>0:
            return loop(n-1, p + n/(n+1))
        else:
            return p
    return loop(n,0)

# while loop
def sum_of_num_over_next(n):
    p = 0
    while n>0:
        n,p = n-1, p + n/(n+1)
    return p
  

# Test code
print(sum_of_num_over_next(0)) # 0
print(sum_of_num_over_next(1)) # 0.5
print(sum_of_num_over_next(3)) # 1.9166666...
print(sum_of_num_over_next(5)) # 3.5500000..
print(sum_of_num_over_next(10)) # 7.98012265..
print(sum_of_num_over_next(100)) # 95.80272149226131...
