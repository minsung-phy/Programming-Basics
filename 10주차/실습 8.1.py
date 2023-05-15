def digit_art_horizontal_left_down(n):
    for i in range(1,n+1):
        for j in range(i+1):
            print(j+1, end=' ')
        print()

# Test code
digit_art_horizontal_left_down(7)

def digit_art_horizontal_left_up(n):
    for i in range(n):
        for j in range(n-i):
            print(j+1, end=' ')
        print()

# Test code
digit_art_horizontal_left_up(7)