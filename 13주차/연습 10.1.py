# 연습 10.1 퍼즐 게임 미니 스도쿠 예외 처리 추가
import random
import time

def initialize_board_4x4(): 
    row0 = [1,2,3,4]
    random.shuffle(row0)
    row1 = row0[2:4] + row0[0:2]
    row2 = [row0[1],row0[0],row0[3],row0[2]]
    row3 = row2[2:4] + row2[0:2]
    return [row0, row1, row2, row3]

def shuffle_ribbons(board):
    top = board[:2]
    bottom = board[2:]
    random.shuffle(top)
    random.shuffle(bottom)
    return top + bottom

def transpose(board):
    size = len(board)
    transposed = [[] for _ in range(size)]
    for row in board:
        for i in range(size):
            transposed[i].append(row[i])
    return transposed

def create_solution_board_4x4():
    board = initialize_board_4x4()
    board = shuffle_ribbons(board)
    board = transpose(board)
    board = shuffle_ribbons(board)
    board = transpose(board)
    return board

def copy_board(board):
    board_clone = []
    for row in board:
        board_clone.append(row[:])
    return board_clone

def get_level():
    print("Enter your level.")
    level = input("Beginner=1, Intermediate=2, Advanced=3: ")
    while level not in ("1","2","3"):
        level = input("Beginner=1, Intermediate=2, Advanced=3: ")
    if level == "1":
        return 6
    elif level == "2":
        return 8
    else:
        return 10
    
def make_holes(board, no_of_holes):
    while no_of_holes > 0:
        i = random.randint(0,3)
        j = random.randint(0,3)
        if board[i][j] != 0:
            board[i][j] = 0
            no_of_holes -= 1  
    return board

def show_board(board):
    for row in board:
        for entry in row:
            if entry == 0:
                print('.', end=' ')
            else:
                print(entry, end=' ')
        print()

def sudoku_4x4():
    solution_board = create_solution_board_4x4()
    puzzle_board = copy_board(solution_board)
    no_of_holes = get_level()
    puzzle_board = make_holes(puzzle_board, no_of_holes)
    show_board(puzzle_board)
    start = time.time()
    while no_of_holes > 0:
        while True:
            try:
                i = int(input("Row#(1,2,3,4): ")) - 1
                j = int(input("Column#(1,2,3,4): ")) - 1
                assert 0 <= i <= 3
                assert 0 <= j <= 3
            except ValueError:
                print("Not a number.")
            except AssertionError:
                print("Not in a range. (range : '1 <= row, column <= 4')")
            else:
                if puzzle_board[i][j] != 0:
                    print("Not empty!")
                    continue
                while True:
                    try:
                        n = int(input("Number(1,2,3,4): "))
                        assert 1 <= n <= 4
                    except ValueError:
                        print("Not a number.")
                    except AssertionError:
                        print("Not in a range. (range : '1 <= Number <= 4')")
                    else:
                        if n == solution_board[i][j]:
                            puzzle_board[i][j] = solution_board[i][j]
                            show_board(puzzle_board)
                            no_of_holes -= 1
                        else:
                            print(n, ": Wrong number! Try again.")
                        break
                    break
                break
    end = time.time()
    print("It took you", round(end - start, 2), "seconds to complete the game.")
    print("Well done! Come again.")

sudoku_4x4()