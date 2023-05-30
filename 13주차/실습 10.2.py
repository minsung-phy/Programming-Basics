def input_float():
    while True:
        try:
            a = float(input("Enter a number: "))
            print(a)
            break
        except ValueError:
            print("Not a number.")

input_float()