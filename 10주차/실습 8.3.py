# 내 풀이
def digit_art_vertical_alternative(n):
    for i in range(n):
        for j in range(n):
            if j % 2 == 0:
                print(i+1, end=' ')
            else:
                print(n-i, end=' ')
        print()

# 솔루션
def digit_art_vertical_alternate(n):
    for i in range(n):
        for j in range(n):
            if j % 2 == 0:
                print(i+1, end=' ')
            else:
                print(n-i, end=' ')
        print()

def digit_art_vertical_alternate(n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if j % 2 == 1:
                print(i,end=' ') 
            else:
                print(n-i+1,end=' ') 
        print()

def digital_art_vertical_alternate(n):
    for i in range(1, n+1):
        for _ in range(n):
            print(i, end = ' ')
            i = n - i + 1
        print()
        
# Test code
digit_art_vertical_alternate(7)