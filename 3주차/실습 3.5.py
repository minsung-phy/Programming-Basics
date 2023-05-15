#실습 3.5

def smallest(x, y, z):
    if x <= y:
        if x <= z:
            return x
        else:
            return z
    else:
        if y <= z:
            return y
        else:
            return z

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
