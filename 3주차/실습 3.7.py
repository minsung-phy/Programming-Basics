#실습 3.7

print("Score Average Calculator")
number = int(input("How many classes? "))
total = 0
count = 0
while count < number:
    score = int(input("Enter your score:"))
    total += score # total = total + score
    count += 1 # count = count + 1
print("Your average score =", end=' ')

if count > 0:
    print(round(total/number, 1))
else:
    print('Your average score = 0.0')
