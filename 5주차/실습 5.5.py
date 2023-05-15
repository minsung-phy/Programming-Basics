# insert 함수
def insert(x,ss):   
    left = []
    while ss != []:
        if x <= ss[0]:
            left.append(x)
            return left + ss
        else:
            left.append(ss[0])
            ss = ss[1:]
    left.append(x)
    return left

# 삽입정렬함수: 꼬리재귀
def insertion_sort(xs):
    def loop(xs, ss):
        if xs !=[]:
            return loop(xs[1:], insert(xs[0], ss))
        else:
            return ss
    return loop(xs,[])


# # Test code
print(insertion_sort([3,5,4,2])) # [2, 3, 4, 5]
    