# 연습 5.6 윤년 출력 프로시저

def is_leap_year(year):
    return year % 400 == 0 or \
           year % 4 == 0 and year % 100 != 0

def print_leap_year(yearfrom, yearto):
    print("Leap years between", yearfrom, "and", yearto, ":")
    for i in range(yearfrom, yearto+1):
        if is_leap_year(i):
            print(i)

# Test code
print_leap_year(1990, 2004) # 1992 1996 2000 2004
print_leap_year(2005, 2014) # 2008 2012
print_leap_year(2094, 2106) # 2096 2104
