while True:
    try:
        x = int(input( ))
        reciprocal = 1 / x
        print("The reciprocal of", x, "is", reciprocal)
        break
    except ValueError:
        print("Not a number.")
    except ZeroDivisionError:
        print("The reciprocal of 0 does not exist.")
        break
    except:
        print("Unexpected exception occurred.")
        break

while True:
    try:
        x = int(input("Enter a number: "))
        reciprocal = 1 / x
        print("The reciprocal of", x, "is", reciprocal)
        break
    except ValueError as message:
        print(message)
    except ZeroDivisionError as message:
        print(message)
        break

while True:
    try:
        x = int(input("Enter a number: "))
        reciprocal = 1 / x
    except ValueError:
        print("Not a number.")
    except ZeroDivisionError:
        print("The reciprocal of 0 does not exist.")
        break
    else: # 예외가 발생하지 않은 경우에만 실행 
        print("The reciprocal of", x, "is", reciprocal)
        break
    finally: # 예외 발생 여부에 상관없이 무조건 실행
        print(":-)")

def fac(n):
    ans = 1
    while n > 1:
        ans = n * ans
        n = n - 1
    return ans

def factorial():
    while True:
        try:
            n = int(input("Enter a number: "))
            assert n >= 1
        except ValueError:
            print("Not a number.")
        except AssertionError:
            print("Not a natural number.")
        else:
            print("factorial(", n, ") = ", fac(n), sep='')
            print("Goodbye!")
            break
        
class NonPositive(Exception): pass

def factorial():
    while True:
        try:
            n = int(input("Enter a number: "))
            if n < 1:
                raise NonPositive
        except ValueError:
            print("Not a number.")
        except NonPositive:
            print("Not a natural number.")
        else:
            print("factorial(", n, ") = ", fac(n), sep='')
            print("Goodbye!")
            break
        