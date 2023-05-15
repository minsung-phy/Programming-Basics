# 연습 5.10

# 재귀 함수 
def updown(ns):
    if ns != []:
        if ns[0] % 2 == 0:
            return [ns[0] // 2] + updown(ns[1:])
        else:
            return [ns[0]*2] + updown(ns[1:])
    else:
        return []

# 꼬리 재귀
def updown(ns):
    def loop(ns, p):
        if ns != []:
            if ns[0] % 2 == 0:
                return loop(ns[1:], p + [ns[0] // 2])
            else:
                return loop(ns[1:], p + [ns[0]*2] )
        else:
            return p
    return loop(ns, [])

# while loop
def updown(ns):
    p = []
    while ns != []:
        if ns[0] % 2 == 0:
            ns, p = ns[1:], p + [ns[0] // 2]
        else:
            ns, p = ns[1:], p + [ns[0]*2]
    return p

# for loop
def updown(ns):
    p = []
    for i in ns:
        if i % 2 == 0:
            p = p + [i // 2]
        else:
            p = p + [i*2]
    return p

# Test code
print(updown([4,6,5,3,7,6,2,1,3,2]))
print(updown([14,69,87,13,0,16,83,19,45,88]))
