import random
import time

def gugudan():
    count = 0
    n = 0
    start = time.perf_counter()
    while count < 5:
        a = random.randint(1, 9)
        b = random.randint(1, 9)
        ans = int(input(str(a) + " X " + str(b) + " = "))
        if ans == a * b:
            n = n + 1
            print("정답입니다!")
        else:
            print("틀렸어요...")
        count = count + 1
    end = time.perf_counter()
    if n == 5:
        print("축하합니다. 만점입니다!")
    elif n == 0:
        print("모두 틀렸습니다 :(")
    else:
        print("5문제에서", n,"개 맞췄습니다.")
    print("(총 소요시간", round(end-start, 2), "초)")

gugudan()