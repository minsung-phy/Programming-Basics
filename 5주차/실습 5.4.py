def insert(x,ss):
    left = []
    while ss != []:
        if x <= ss[0]:
            left.append(x)
            return left+ss
        else:
            left.append(ss[0])
            ss = ss[1:]
    left.append(x)
    return left


print(insert(6,[2,4,5,7,8]))