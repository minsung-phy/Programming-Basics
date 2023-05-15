def transpose(board):
    size = len(board)
    transposed = [[] for _ in range(size)]
    for row in board:
        for i in range(size):
            transposed[i].append(row[i])
    return transposed

# Test code
a = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print(transpose(a))