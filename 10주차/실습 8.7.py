import random

def make_holes(board, no_of_holes):
    while no_of_holes > 0:
        i = random.randint(0,3)
        j = random.randint(0,3)
        if board[i][j] != 0:
            board[i][j] = 0
            no_of_holes -= 1        
    return board

b1 = [[170, 45, 75, 90], [2, 24, 802, 66]]

print(make_holes(b1, 2))