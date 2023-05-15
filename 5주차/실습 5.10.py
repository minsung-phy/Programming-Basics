def partition(pivot,xs):
    def loop(xs,left,right):
        if xs != []:
            if xs[0] <= pivot:
                left.append(xs[0])
            else:
                right.append(xs[0])
            return loop(xs[1:],left,right)
        else:
            return left, right
    return loop(xs,[],[]) 

print(partition(5,[7,2,1,9,4]))
print(partition(3,[5]))