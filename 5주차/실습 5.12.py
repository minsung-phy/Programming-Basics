def partition(pivot,xs):
    left, right = [], []
    for x in xs:
        if x <= pivot:
            left.append(x)
        else:
            right.append(x)
    return left, right

print(partition(5,[7,2,1,9,4]))
print(partition(3,[5]))