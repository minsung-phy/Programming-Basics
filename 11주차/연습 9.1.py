def sparse(ns):
    dic = {}
    index = 0
    for n in ns:
        if n != 0:
            dic[index] = n
        index += 1
    return dic

# Test code
print(sparse([])) 
print(sparse([0,0,3,0,0,0,0,0,0,7,0,0])) 
print(sparse([1,0,2,0,0,0,9,0,0]))