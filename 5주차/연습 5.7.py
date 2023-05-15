# 연습 5.7 ISBN-10 코드 검증

def isbn10(s):
    total = 0
    for i in range(1,10):
        total = total + int(s[i-1]) * i
    last = total % 11
    if last == 10:
        return s[9] == "X"
    else:
        return s[9] == str(last)

# Test code
print(isbn10("123456789X")) # True
print(isbn10("1234567890")) # False
print(isbn10("1413304540")) # True
print(isbn10("141330454X")) # False
