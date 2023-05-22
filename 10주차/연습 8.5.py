import random

def lotto645():
    numbers = []
    for _ in range(6):
        number = random.randrange(1,46)
        while number in numbers: # 중복되는 숫자 나오지 않게 하려고
           number = random.randrange(1,46)
        numbers.append(number)
    numbers.sort()
    for number in numbers:
        if number < 10:
            print("0" + str(number), end=" ")
        else:
            print(number, end=" ")
    print()

