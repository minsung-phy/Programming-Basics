import random

# 중첩 루프
couples = []
for c in ["a", "b"]:
    for n in range(3):
        couple = (c, n)
        couples.append(couple)
## print(couples)

# 가로 아스키 아트
def digit_art_horizontal(n):
    for _ in range(n):
        for i in range(n):
            print(i+1, end=' ')
        print()

# 실습 8.1 가로변형
def digit_art_horizontal_left_down(n):
    for i in range(n):
        for j in range(0,i+1):
            print(j+1, end=' ')
        print()

def digit_art_horizontal_left_up(n):
    for i in range(n):
        for j in range(0,n-i):
            print(j+1, end=' ')
        print()

# 세로
def digit_art_vertical(n):
    for i in range(n):
        for j in range(n):
            print(i+1, end=' ')
        print()

# 실습 8.2 세로 변형
def digit_art_vertical_right_down(n):
    for i in range(n):
        for j in range(n):
            if n - 1 - i > j:
                print(' ', end=' ')
            else:
                print(i+1, end=' ')
        print()

# 방향 바꾸기
def digit_art_horizontal_alternate(n):
    for i in range(n):
        for j in range(n):
            if i % 2 == 0:
                print(j+1, end=' ')
            else:
                print(n-j, end=' ')
        print()

# 실습 8.3 세로 방향 바꾸기
def digit_art_vertical_alternate(n):
    for i in range(n):
        for j in range(n):
            if j % 2 == 0:
                print(i+1, end=' ')
            else:
                print(n-i, end=' ')
        print()
    
# 실습 8.4 버블정렬 구현
def bubblesort(ns):
    for k in range(len(ns)-1, 0, -1):
        for i in range(k):
            if ns[i] > ns[i+1]:
                ns[i], ns[i+1] = ns[i+1], ns[i]
    return ns

print(bubblesort([32,23,18,7,11,99,55]))  # [7, 11, 18, 23, 32, 55, 99]

# 실습 8.5 기수정렬 구현
def radixsort(ds):
    if ds != []:
        length = len(ds[0])
        for i in range(length - 1, -1, -1):
            distributed = [[] for _ in range(10)]
            for d in ds:
                distributed[int(d[i])].append(d)
            ds = []
            for d in distributed:
                ds += d
        return ds
    else:
        return []
    
## 이 코드는 주어진 리스트 ds를 기수 정렬을 사용하여 정렬합니다.
## 기수 정렬은 각 값을 자리수별로 분해하여 정렬하는 방식입니다. 이때, 각 자리수를 비교해 가며 정렬하므로 안정 정렬에 속합니다.
## 이 코드에서는 먼저, 주어진 리스트 ds 중 가장 긴 원소의 자리수를 찾습니다. 그리고 이 자리수부터 가장 작은 자리수까지(여기서는 0) 반복문을 돌면서 각 자리수별로 정렬합니다.
## 각 자리수별로 정렬은 다음과 같이 이루어집니다.
## 0~9까지의 리스트 distributed를 만듭니다.
## ds에서 각 원소를 자리수(i)에 따라 분배합니다. 예를 들어, ds에 있는 원소 중 자리수 i가 3이면, distributed의 3번째 리스트에 해당 원소를 추가합니다. 이렇게 하면 distributed[0]에는 ds에서 0이 있는 원소들, distributed[1]에는 1이 있는 원소들 등이 들어갑니다.
## 분배된 원소들을 순서대로 다시 ds에 추가합니다.
## ds가 정렬된 결과를 가지고 다음 자리수(i-1)에 대한 정렬을 수행합니다.
## 각 자리수별로 위의 과정을 반복하면, 최종적으로 ds는 기수 정렬 알고리즘에 따라 정렬된 결과를 가지게 됩니다.

# 스도쿠 정답보드 만들기
def initialize_board_4x4():
    row0 = [1, 2, 3, 4]
    random.shuffle(row0)
    row1 = row0[2:4] + row0[0:2]
    row2 = [row0[1], row0[0], row0[3], row0[2]]
    row3 = row2[2:4] + row2[0:2]
    return [row0, row1, row2, row3]

def shuffle_ribbons(board):
    top = board[:2]
    bottom = board[2:]
    random.shuffle(top)
    random.shuffle(bottom)
    return top + bottom

# 실습 8.6 가로세로 뒤집기
def transpose(board):
    size = len(board)
    transposed = [[] for _ in range(size)]
    for row in board:
        for i in range(size):
            transposed[i].append(row[i])
    return transposed

# 스도쿠 정답보드 무작위로 만들기
def create_solution_board_4x4():
    board = initialize_board_4x4()
    board = shuffle_ribbons(board)
    board = transpose(board)
    board = shuffle_ribbons(board)
    board = transpose(board)
    return board

# 메인 프로시저 구현
def sudoku_mini():
    solution_board = create_solution_board_4x4()
    puzzle_board = copy_board(solution_board)
    no_of_holes = get_level()
    puzzle_board = make_holes(puzzle_board, no_of_holes)
    show_board(puzzle_board)
    while no_of_holes > 0:
        i = get_integer("Row#(1,2,3,4): ",1,4) - 1
        j = get_integer("Column#(1,2,3,4): ",1,4) - 1
        if puzzle_board[i][j] != 0:
            print("Not empty!")
            continue
        n = get_integer("Number(1,2,3,4): ",1,4) 
        if n == solution_board[i][j]:
            puzzle_board[i][j] = solution_board[i][j]
            show_board(puzzle_board)
            no_of_holes -= 1
        else:
            print(n, ": Wrong number! Try again.")
    print("Well done! Come again.")

# 중첩 리스트 복제 함수
def copy_board(board):
    board_clone = []
    for row in board:
        board_clone.append(row[:])
    return board_clone

# 난이도 입력 받기
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
    
# 실습 8.7 퍼즐보드 만들기
def make_holes(board, no_of_holes):
    while no_of_holes > 0:
        i = random.randint(0,3)
        j = random.randint(0,3)
        if board[i][j] != 0:
            board[i][j] = 0
            no_of_holes = no_of_holes - 1
    return board

# 퍼즐보드 보여주기
def show_board(board):
    for row in board:
        for entry in row:
            if entry == 0:
                print('.', end=' ')
            else:
                print(entry, end=' ')
        print()

# 숫자 입력받기
def get_integer(message, i, j):
    number = input(message)
    while not (number.isdigit() and i <= int(number) <= j):
        number = input(message)
    return int(number)

sudoku_mini()

# 연습 8.5 로또 6/45
## 나의 답
def lotto645():
    for _ in range(6):
        numbers = []
        numbers2 = []
        for _ in range(6):
            k = random.randrange(1,46)
            while k in numbers2:
                k = random.randrange(1,46)
            numbers2.append(k)
            if k < 10:
                k = "0" + str(k)
            else:
                k = str(k)
            numbers.append(k)
        numbers.sort()
        print(numbers)

## 솔루션
def lotto645():
    numbers = []
    for _ in range(6):
        number = random.randrange(1,46)
        while number in numbers:
            number = random.randrange(1,46)
        numbers.append(number)
    numbers.sort
    for number in numbers:
        if number < 10:
            print("0" + str(number), end=" ")
        else:
            print(number, end=" ")
    print()