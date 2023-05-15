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

# 삽입정렬 함수 for loop
def insertion_sort(xs):
    ss = []
    for x in xs:
        ss = insert(x,ss)
    return ss


# # Test code
print(insertion_sort([3,5,4,2])) # [2, 3, 4, 5]