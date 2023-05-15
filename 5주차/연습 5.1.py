# 연습 5.1 팰린드롬 검사 함수

def ispalindrome(s):
    if len(s) <= 1:
        return True
    elif s[0] != s[-1]:
        return False
    else:
        return ispalindrome(s[1:-1])

def ispalindrome(s):
    return (len(s) <= 1 or (s[0] == s[-1] and ispalindrome(s[1:-1])))

print(ispalindrome("aaaaa"))
print(ispalindrome("이민성"))
