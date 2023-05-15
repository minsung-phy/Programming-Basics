def find_1st(filename, x):
    infile = open(filename, "r")
    outfile = open("result.txt", "w")
    text = infile.read()
    position = text.find(x)
    if position == -1:
        outfile.write(x + " is not found.\n")
    else:
        outfile.write(x + " is at " + str(position) + " the 1st time.\n")
    outfile.close()
    infile.close()
    print("Done")

# Test code
find_1st("article.txt",'computer')    

