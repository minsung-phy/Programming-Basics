#실습 2.5

def fahrenheit2celsius(f):
    return (f - 32) * 5 / 9

print("Fahrenheit to Celsius conversion")

f = int(input("Degerees in Fahrenheit? "))
degrees = round(fahrenheit2celsius(f), 1)
print(degrees,"degrees in celsius")
