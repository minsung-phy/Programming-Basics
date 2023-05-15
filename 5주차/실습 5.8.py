def merge(left, right):
    def loop(left, right, ss):
        if not (left == [] or right == []):
            if left[0] <= right[0]:
                ss.append(left[0])
                return loop(left[1:], right, ss)
            else:
                ss.append(right[0])
                return loop(right[1:], left, ss)
        else:
            return ss + left + right
    return loop(left, right, [])


# # Test code
print(merge([18,23,32],[7,11,55,99])) # [7, 11, 18, 23, 32, 55, 99]