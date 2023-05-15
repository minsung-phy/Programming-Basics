## 무작위 구구단 완성하기 (지금까지 작성한 내용으로 gugudan 함수를 완성해서 제출하세요.)
# 5번 구구단 문제를 물어봅니다.
# 각 문제를 풀 때마다 정답/오답 여부를 알려줍니다.
# 다섯 문제를 모두 풀면 몇 문제를 맞췄는지 문구를 출력하고 시간이 총 얼마 걸렸는지 알려줍니다.
# 맞춘 문제 수에 따라 서로 다른 내용을 출력해야 합니다. (기본, 모두 맞췄을 때, 모두 틀렸을 때)

import time
import random

def rand_gugu():
    count = 0
    ans = 0
    total = 0
    while count < 5:
        a = random.randint(1, 9)
        b = random.randint(1, 9)
        start = time.perf_counter()
        mul = int(input(str(a) + " x " + str(b) + " = "))
        end = time.perf_counter()
        elapsed = end - start
        if mul == a * b: 
            ans = ans + 1
            print("정답입니다!")
        else:
            print("틀렸어요...")
        count += 1
        total += elapsed
    if ans == 5:
        print("축하합니다. 만점입니다!")
    elif 0 < ans < 5:
        print("5문제에서", ans, "개 맞췄습니다.")
    else:
        print("모두 틀렸습니다 :(")
    print("(총 소요시간", round(total, 2), "초)")
    
rand_gugu()