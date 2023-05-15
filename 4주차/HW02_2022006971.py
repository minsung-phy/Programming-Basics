# 2023 CSE1017 HW02
# name : 이민성
# student id : 2022006971
#
####

### 3.4 - median (p.133-134)
def smaller(x,y):
    if x < y:
        return x
    else:
        return y

def smallest(x,y,z):
    if x < y:
        if x < z:
            return x
        else:
            return z
    else:
        if y < z:
            return y
        else:
            return z

def median(x,y,z):
    one = smallest(x,y,z)
    if one == x:
        return smaller(y,z)
    elif one == y:
        return smaller(x,z)
    else:
        return smaller(x,y)

# # Test code
print(median(1,3,5)) # 3
print(median(3,5,1)) # 3
print(median(3,3,3)) # 3
print(median(3,5,3)) # 3
print(median(3,5,5)) # 5

### 3.5 - smallest_odd (p.134-135)

def even(x):
    return x % 2 == 0

def smaller_odd(x,y):
    if even(x) and even(y):
        return None
    elif even(x):
        return y
    elif even(y):
        return x
    else:
        if x <= y:
            return x
        else:
            return y
        
def smallest_odd(x,y,z):
    smaller = smaller_odd(x,y)
    if smaller == None:
        if even(z):
            return None
        else:
            return z
    else:
        return smaller_odd(smaller,z)

# # Test code
print(smallest_odd(3,2,2))  # 3
print(smallest_odd(3,5,7))  # 3
print(smallest_odd(3,5,1))  # 1
print(smallest_odd(8,3,4))  # 3
print(smallest_odd(8,3,5))  # 3
print(smallest_odd(8,5,3))  # 3
print(smallest_odd(2,8,3)) # 3
print(smallest_odd(2,8,4))  # None

### 4.2 - factorial (p.197-198)
# factorial : recursive version
# def fac(n):
#     if n > 0:
#         return fac(n-1) * n
#     else:
#         return 1

# factorial : tail-recursive version
def fac_t(n):
    def loop(n,p):
        if n > 0:
            return loop(n-1, p*n)
        else:
            return p
    return loop(n, 1)

# # Test code
print(fac_t(0))  # 1
print(fac_t(1))  # 1
print(fac_t(5))  # 120
print(fac_t(9))  # 362880
print(fac_t(15)) # 1307674368000
print(fac_t(30)) # 265252859812191058636308480000000

# factorial : while-loop version
def fac_w(n):
    ans = 1
    while n > 0:
        n, ans = n - 1, ans * n
    return ans

# # Test code
print(fac_w(0))  # 1
print(fac_w(1))  # 1
print(fac_w(5))  # 120
print(fac_w(9))  # 362880
print(fac_w(15)) # 1307674368000
print(fac_w(30)) # 265252859812191058636308480000000
