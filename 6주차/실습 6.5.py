# 내 코드
def find_all(filename, x):
    infile = open(filename, "r")
    outfile = open("result.txt", "w")
    text = infile.read()
    position = text.find(x)
    if position == -1:
        outfile.write(x + " is not found.\n")
    else:
        outfile.write("at " + str(position))
        while 1:
            position = text.find(x, position+1)
            if position == -1:
                outfile.write(".")
                break
            else:
                outfile.write(", " + str(position))
    outfile.close()
    infile.close()
    print("Done")

# 솔루션
def find_all(filename,key) :
    infile = open(filename,"r")
    outfile = open("result.txt","w")
    text = infile.read()
    position = text.find(key)
    if position == -1:
        outfile.write(key + " is not found.\n")
    while position != -1 :
        outfile.write(key + " is at " + str(position) + ".\n")
        position = text.find(key,position+1)
    outfile.close()
    infile.close()
    print("Done")

# Test code
find_all("article.txt", 'computer')

