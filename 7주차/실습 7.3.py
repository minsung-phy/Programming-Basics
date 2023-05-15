### 실습 7.3 - 표채워풀기 알고리즘 구현 (p.357)

def minsteps(n):
    memo = [0 for _ in range(n+1)]
    for i in range(2,n+1):
        steps = memo[i-1]
        if i % 2 == 0:
            steps = min(steps, memo[i//2])
        if i % 3 == 0:
            steps = min(steps, memo[i//3])
        memo[i] = steps + 1
    return memo[n]

def run_minsteps(n):
    from time import perf_counter
    start = perf_counter()
    answer = minsteps(n)
    finish = perf_counter()
    print("minsteps(", n, ") => ", answer, sep="")
    print(round(finish-start), "seconds")

## Test code
print(run_minsteps(3))       # 1
print(run_minsteps(4))       # 2
print(run_minsteps(7))       # 3
print(run_minsteps(10))      # 3
print(run_minsteps(23))      # 6
print(run_minsteps(237))     # 8
print(run_minsteps(317))     # 10
print(run_minsteps(514))     # 8
print(run_minsteps(711))     # 9
print(run_minsteps(908))     # 11
print(run_minsteps(1000))    # 9
print(run_minsteps(2020))    # 10
print(run_minsteps(1111111)) # 19