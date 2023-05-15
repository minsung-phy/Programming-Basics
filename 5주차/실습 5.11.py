def partition(pivot,xs):
    left, right = [], []
    while xs != []:
        if xs[0] <= pivot:
            left.append(xs[0])
        else:
            right.append(xs[0])
        xs = xs[1:]
    return left, right

print(partition(5,[7,2,1,9,4]))
print(partition(3,[5]))