### 실습 7.2 - comb_pascal 함수의 실행 시간 측정 (p.349)

def comb_pascal(n, r):
    row0 = [1 for _ in range(r+1)]
    matrix = [row0] + [[1] for _ in range(n-r)]
    for i in range(1, n - r + 1):
        for j in range(1, r + 1):
            newvalue = matrix[i][j - 1] + matrix[i - 1][j]
            matrix[i].append(newvalue)
    return matrix[n - r][r]

def run_comb_pascal(n,r):
    from time import perf_counter
    start = perf_counter()
    answer = comb_pascal(n,r)
    finish = perf_counter()
    print("comb_pascal(", n, ",", r, ") => ", answer, sep="")
    print(round(finish-start,4), "seconds")

## Test code
run_comb_pascal(30,3)  # 4060 - 0.0 seconds
run_comb_pascal(30,27) # 4060 - 0.0 seconds
run_comb_pascal(30,7)  # 2035800 - 0.0001 seconds
run_comb_pascal(30,23) # 2035800 - 0.0 seconds
run_comb_pascal(30,10) # 30045015 - 0.0001 seconds
run_comb_pascal(30,20) # 30045015 - 0.0001 seconds
run_comb_pascal(30,15) # 155117520 - 0.0001 seconds