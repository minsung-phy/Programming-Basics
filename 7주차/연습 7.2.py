def change(n):
    table = [0,1,1,2,2,1,2,1] 
    for i in range(8,n+1):
        smallest = min(table[i-1],table[i-2],table[i-5],table[i-7])
        table.append(smallest + 1)
    return table[n]

# Test code
for i in range(1,29): 
    print(i, change(i))