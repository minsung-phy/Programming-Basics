def comb_pascal(n,r):
    row0 = [1 for _ in range(r+1)]
    matrix = [row0] + [[1] for _ in range(n-r)]
    for i in range(1, n-r+1):
        for j in range(1, r+1):
            newvalue = matrix[i][j-1] + matrix[i-1][j]
            matrix[i].append(newvalue)
    return matrix[n-r][r]

print("This program computes combination of two natural numbers, n and r.")
print("press Control+C to quit")
while True:
    try:
        n = int(input("Enter n: "))
        r = int(input("Enter r: "))
        assert n, r >= 0 
        assert n > r
    except ValueError:
        print("Must be a number.")
    except AssertionError:
        print(n, "C", r, " is not defined.", sep='')
    except KeyboardInterrupt:
        print("Goodbye!")
        break
    else:
        ans = comb_pascal(n,r)
        print(n, "C", r, " = ", ans, sep='')
