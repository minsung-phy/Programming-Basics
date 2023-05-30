class NonRange(Exception): pass

def input_float_one():
    while True:
        try:
            a = float(input("Enter a number: "))
            if a < -1.0 or a > 1.0 :
                raise NonRange
            print(a)
            break
        except ValueError:
            print("Not a number.")
        except NonRange:
            print('Out of range. range is "-1.0 ~ 1.0"')

input_float_one()