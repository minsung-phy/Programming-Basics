# 연습 4.7 정수 범위의 합

# 재귀 함수 
def add_range(start,stop,step):
    if start < stop:
        return start + add_range(start+step,stop,step)
    else:
        return 0

# 꼬리 재귀
def add_range(start,stop,step):
    def loop(start, p):
        if start < stop:
            return loop(start+step, p+start)
        else:
            return p
    return loop(start, 0)

# while loop
def add_range(start,stop,step):
    p = 0
    while start < stop:
        start, p = start+step, p+start
    return p

# Test code
print(add_range(1,10,1)) # 45
print(add_range(1,10,2)) # 25
print(add_range(1,10,3)) # 12
print(add_range(-5,6,2)) # 0
