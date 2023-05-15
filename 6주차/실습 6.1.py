def bin_search_OX(ss,x):
    mid = len(ss) // 2
    return ss != [] and \
           (x == ss[mid] or \
            x < ss[mid] and bin_search_OX(ss[:mid],x) or \
            bin_search_OX(ss[mid+1:],x))

# Test code
s = [3,5,8,7,4,6,1,9,2]
s.sort()
print(bin_search_OX(s,5))  # True
print(bin_search_OX(s,8))  # True
print(bin_search_OX(s,1))  # True
print(bin_search_OX(s,11)) # False
 