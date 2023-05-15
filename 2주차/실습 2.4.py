#실습 2.4

def coin_in_total(c500, c100, c50, c10):
    return c500 * 500 + c100 * 100 + c50 * 50 + c10 * 10

print("Enter the number of coins you have.")
c500 = int(input("500 won? "))
c100 = int(input("100 won? "))
c50 = int(input("50 won? "))
c10 = int(input("10 won? "))
total = coin_in_total(c500, c100, c50, c10)
print("You have", total, "won in total.") 
