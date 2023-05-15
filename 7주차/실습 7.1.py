### 실습 7.1 - comb 함수의 실행 시간 측정 함수

def comb(n,r):
    if r != 0 and r != n:
        return comb(n-1,r-1) + comb(n-1,r)
    else:
        return 1

## Test code
print(comb(30,3))  # 4060
print(comb(30,27)) # 4060
print(comb(30,7))  # 2035800
print(comb(30,23)) # 2035800
print(comb(30,10)) # 30045015 - 좀 오래 걸림
print(comb(30,20)) # 30045015 - 좀 오래 걸림
print(comb(30,15)) # 155117520 - 매우 오래 걸림

def run_comb(n,r):
    from time import perf_counter
    start = perf_counter()
    answer = comb(n,r)
    finish = perf_counter()
    print("comb(", n, ",", r, ") => ", answer, sep="")
    print(round(finish-start,4), "seconds")

## Test code
run_comb(30,3)  # 4060 - 0.001 seconds
run_comb(30,27) # 4060 - 0.0011 seconds
run_comb(30,7)  # 2035800 - 0.5204 seconds
run_comb(30,23) # 2035800 - 0.5472 seconds
run_comb(30,10) # 30045015 - 7.8143 seconds
run_comb(30,20) # 30045015 - 7.9519 seconds
run_comb(30,15) # 155117520 - 41.1853 seconds