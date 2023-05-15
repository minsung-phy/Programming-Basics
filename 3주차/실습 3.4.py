#실습 3.4

def smaller(x, y):
    if x <= y:
        return x
    else:
        return y

# Test code
print(smaller(3,5)) #3
print(smaller(5,3)) #3
print(smaller(3,3)) #3
print(smaller(9,4)) #4
