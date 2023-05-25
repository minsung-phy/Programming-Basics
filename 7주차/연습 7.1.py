def minbags(n):
    if n > 1:
        if n == 2 or n == 3 or n == 5:
            return 1
        else:
            smallest = minbags(n-2)
            if n > 4:
                smallest = min(smallest, minbags(n-3))
            if n > 6:
                smallest = min(smallest, minbags(n-5))
        return 1 + smallest
    else:
        return 0
    
def run_minbags(n):
    from time import perf_counter
    start = perf_counter()
    answer = minbags(n)
    finish = perf_counter()
    print("minbags(", n, ") => ", answer, sep="")
    print(round(finish-start,1), "seconds")

# 표채워풀기 버전
def minbags(n):
    table = [0,0,1,1,2,1,2]
    for i in range(7,n+1):
        smallest = min(table[i-2], table[i-3], table[i-5])
        table.append(smallest + 1)
    return table[n]

# Test code
for i in range(36,51):
    run_minbags(i)
