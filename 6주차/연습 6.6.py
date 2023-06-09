def isanagram(word1,word2):
    while word1 != '':
        if word1[0] in word2:
            index = word2.find(word1[0])
            word1 = word1[1:]
            word2 = word2[:index] + word2[index+1:]
        else:
            return False
    return word2 == ''
            
## Test code
print(isanagram('',''))                 # True
print(isanagram('z','z'))               # True
print(isanagram('zz','z'))              # False
print(isanagram('z','zz'))              # False
print(isanagram('silent','listen'))     # True
print(isanagram('silent','listens'))    # False
print(isanagram('elvis','lives'))       # True
print(isanagram('restful','fluster'))   # True
print(isanagram('restfully','fluster')) # False
print(isanagram('문전박대','대박전문'))      # True