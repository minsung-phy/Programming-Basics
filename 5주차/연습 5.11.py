def drop_before(s, index):
    if s!= [] and index > 0:
        return drop_before(s[1:], index-1)
    else:
        return s
    
def take_before(s, index):
    if s != [] and index > 0:
        return [s[0]] + take_before(s[1:],index-1)
    else:
        return []
    
def take_before(s, index):
    def loop(s, index, n):
        if s != [] and index > 0:
            return loop(s[1:], index-1, n+[s[0]])
        else:
            return n
    return loop(s, index, [])
    
def take_before(s, index):
    n = []
    while s != [] and index > 0:
        s, index, n = s[1:], index-1, n+[s[0]]
    return n

def sublist(s, low, high):
    if low < 0:
        low = 0
    if high < 0:
        high = 0
    if low <= high:
        return take_before(drop_before(s,low),high-low)
    else:
        return []
    
# Test code
s = [1,2,3,4,5]
print(sublist(s,2,4))
print(sublist(s,0,0))
print(sublist(s,3,6))
print(sublist(s,-3,-2))