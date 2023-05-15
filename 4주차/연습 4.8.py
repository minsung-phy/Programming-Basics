# 연습 4.8 오늘부터 n일 뒤는 몇 년 몇 월 며칠?

# 보조 함수 3개 (월별로 날짜수가 다른 사실과 평년/운년에 따라 2월의 날짜수도 다른 점을 고려하기 위한 함수들
def isleapyear(year):
    # assume year >= 0
    return year % 400 == 0 or \
           year % 4 == 0 and year % 100 != 0

def next_month(year, month):
    # assume year >= 0 and 1 <= month <= 12
    if month == 12:
        year += 1
        month = 1
    else:
        month += 1
    return (year, month)

def days_in_month(year, month):
    # assume year >= 0 and 1 <= month <= 12
    if month == 1 or month == 3 or month == 5 or month == 7 or \
       month == 8 or month == 10 or month == 12:
        return 31
    elif month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    elif month == 2:
        if isleapyear(year):
            return 29
        else:
            return 28

# date_after_n_days 함수
def date_after_n_days(year, month, day, n):
    # assume that is_valid_date(year, month, day) is True
    days_left = days_in_month(year,month) - day
    if days_left < n:
        n -= days_left
        (year, month) = next_month(year, month)
        days_this_month = days_in_month(year, month)
        while days_this_month < n:
            n -= days_this_month
            (year, month) = next_month(year, month)
            days_this_month = days_in_month(year,month)
        return (year, month, n)
    else:
        return (year, month, day + n)

# Test code   
print(date_after_n_days(2019,4,20,2))    # (2019, 4, 22)
print(date_after_n_days(2019,4,20,7))    # (2019, 4, 27)
print(date_after_n_days(2019,4,20,10))   # (2019, 4, 30)
print(date_after_n_days(2019,4,20,11))   # (2019, 5, 1)
print(date_after_n_days(2019,4,20,50))   # (2019, 6, 9)
print(date_after_n_days(2019,4,20,100))  # (2019, 7, 29)
print(date_after_n_days(2019,4,20,200))  # (2019, 11, 6)
print(date_after_n_days(2019,4,20,300))  # (2020, 2, 14)
print(date_after_n_days(2019,4,20,1000)) # (2022, 1, 14)
