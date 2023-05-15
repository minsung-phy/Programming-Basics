#실습 2.6

def complement_nine(n):
    return 10 ** len(str(n)) - 1 - n

print(complement_nine(0)) # 9
print(complement_nine(9)) # 0
print(complement_nine(4)) # 5
print(complement_nine(18)) # 81
print(complement_nine(40)) # 59
print(complement_nine(307)) # 692
print(complement_nine(9142)) # 857
print(complement_nine(9965)) # 34
print(complement_nine(9999)) # 0
