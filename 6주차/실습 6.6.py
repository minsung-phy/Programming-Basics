# 내 코드
def find_all_count(filename, x):
    infile = open(filename, "r")
    outfile = open("result.txt", "w")
    text = infile.read()
    position = text.find(x)
    count = 0
    if position == -1:
        outfile.write(x + " is not found. # " + str(count) + " time(s)\n")
    else:
        outfile.write("at " + str(position))
        count += 1
        while 1:
            position = text.find(x, position+1)
            if position == -1:
                outfile.write(".")
                break
            else:
                outfile.write(", " + str(position))
                count += 1
        outfile.write(" # " + str(count) + " time(s)\n")
    outfile.close()
    infile.close()
    print("Done")

# 솔루션
def find_all_count(filename,key) :
    infile = open(filename,"r")
    outfile = open("result.txt","w")
    text = infile.read()
    position = text.find(key)
    count = 0
    while position != -1 :
        outfile.write(key + " is at " + str(position) + ".\n")
        count += 1
        position = text.find(key,position+1)
    outfile.write(key + " is found " + str(count) + " time(s).\n")
    outfile.close()
    infile.close()
    print("Done")

# Test code 
find_all_count('article.txt', 'computer')


