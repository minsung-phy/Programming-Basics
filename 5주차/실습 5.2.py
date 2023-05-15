def insert(x,ss):
    if ss != []:
        if x <= ss[0]:
            return [x] + ss
        else:
            return [ss[0]] + insert(x,ss[1:])
    else:
        return [x]

# Test code    
print(insert(6,[2,4,5,7,8]))