def bubblesort(ns):
    for k in range(len(ns)-1, 0, -1):
        for i in range(k):
            if ns[i] > ns[i+1]:
                ns[i], ns[i+1] = ns[i+1], ns[i]
    return ns

# Test code
print(bubblesort([32,23,18,7,11,99,55]))  # [7, 11, 18, 23, 32, 55, 99]