#실습 3.6

def smaller(x, y):
    if x <= y:
        return x
    else:
        return y
    
def smallest(x, y, z):
    return smaller(smaller(x,y),z)

# Test code
print(smallest(3,5,9)) # 3
print(smallest(5,3,9)) # 3
print(smallest(5,9,3)) # 3
print(smallest(3,9,5)) # 3
print(smallest(9,3,5)) # 3
print(smallest(9,5,3)) # 3
print(smallest(3,3,5)) # 3
print(smallest(5,3,3)) # 3
print(smallest(3,5,3)) # 3
print(smallest(3,3,3)) # 3
