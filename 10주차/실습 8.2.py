# 내 풀이
def digit_art_horizontal_right_down(n):
    for i in range(n):
        print(" " * 2 * (n-(i+1)), end = '')
        for j in range(i+1):
            print(i+1, end=' ')
        print()

# 솔루션
def digit_art_vertical_right_down(n):
    for i in range(n):
        for j in range(n):
            if n - 1 - i > j:
                print(' ', end=' ')
            else:
                print(i+1, end=' ')
        print()

def digit_art_vertical_right_down(n):
    for i in range(1,n+1):
        for _ in range(n-i):
            print(' ', end=' ')
        for _ in range(i):
            print(i,end=' ') 
        print()

def digit_art_vertical_right_down(n):
    for i in range(1,n+1):
        print("  " * (n-i) + (str(i) + " ") * i)

# Test code
digit_art_vertical_right_down(7)