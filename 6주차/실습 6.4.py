def find_last(filename, x) :
    infile = open(filename,"r")
    outfile = open("result.txt","w")
    text = infile.read()
    found_most_recent = -1
    position = text.find(x)
    while position != -1 :
        found_most_recent = position
        position = text.find(x,position+1)
    if found_most_recent == -1:
        outfile.write(x + " is not found.\n")
    else:
        outfile.write(x + " is at " + str(found_most_recent) + " the last time.\n")
    outfile.close()
    infile.close()
    print("Done")

# Test code
find_last("article.txt", 'computer')   

