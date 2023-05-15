def insert(x,ss):
    def loop(ss,left):
        if ss != []:
            if x <= ss[0]:
                left.append(x)
                return left+ss
            else:
                left.append(ss[0])
                return loop(ss[1:],left)
        else:
            left.append(x)
            return left
    return loop(ss,[])


print(insert(6,[2,4,5,7,8]))