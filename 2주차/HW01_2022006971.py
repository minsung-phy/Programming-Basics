# 2023 CSE1017 HW01
# name : 이민성
# student id : 2022006971
#
####

# 2.1
def celsius2fahrenheit(c):
    return 9 / 5 * c + 32
    
# Test code
print(celsius2fahrenheit(19.4)) # 66.92
print(round(celsius2fahrenheit(19.4), 1)) # 66.9


# 2.2
# 가. 함수 구현
def monthly_payment_plan(principal, interest, year):
    rate_monthly = interest / 100 / 12
    compound = (1 + rate_monthly) ** (year * 12)
    return int(compound * principal * rate_monthly / (compound - 1))

# Test code
print(monthly_payment_plan(10000000, 2.8, 4)) # 220460

# 나. 서비스 구현

print("자유은행 대출 상환금 계산 서비스에 오심을 환영합니다.")
i = int(input("대출원금이 얼마인가요? (백만원 이상) "))
j = float(input("연 이자율은 몇 %인가요? (0.0~9.9) "))
k = int(input("상환기간은 몇 년인가요? "))

print()
print("대출 상환금 내역을 알려드리겠습니다.")
print("대출원금: ", i, "원")
print("연 이자율 ", j, "매월", monthly_payment_plan(i, j, k), "원씩 지불하셔야 합니다.")
print("상환 완료시까지 총 상환금액은", monthly_payment_plan(i, j, k) * 12 * k , "원입니다.")
print()
print("저희 자유은행 항상 여러분과 함께 합니다.")
print("또 들려주세요.")
