# 연습 4.1

# countdown 꼬리 재귀
from time import sleep
def countdown(n):
    if n > 0:
        print(n)
        sleep(1)
        countdown(n-1)
    else:
        print("Lanuch!")

# countdown while loop
from time import sleep
def countdown(n):
    while n > 0:
        print(n)
        sleep(1)
        n = n-1
    print("Lanuch!")

# even 함수
def even(n):
    return n % 2 ==0

# countdown2 
## 자연수 n을 인수로 받아 n부터 1씩 줄여가면서 화면에 1초에 하나씩 프린트한다.
## 0이 되면 launch!를 프린트한다.
## n이 10미만이 되면 n이 짝수일 때 n 대신 Launch Imminent!를 프린트한다.

# countdown2 꼬리 재귀
from time import sleep
def countdown2(n):
    if n > 0:
        if n >= 10:
            print(n)
            sleep(1)
            countdown2(n-1)
        else:
            if even(n):
                print("Launch Imminent!")
                sleep(1)
                countdown2(n-1)
            else:
                print(n)
                sleep(1)
                countdown2(n-1)       
    else:
        print("Lanuch!")

# countdown2 while loop
from time import sleep
def countdown2(n):
    while n > 0:
        if n >= 10:
            print(n)
            sleep(1)
            n = n-1
        else:
            if even(n):
                print("Launch Imminent!")
                sleep(1)
                n = n-1
            else:
                print(n)
                sleep(1)
                n = n-1     
    print("Lanuch!")

# Test Code
print(countdown2(15))
