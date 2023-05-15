def isisogram(word):
    while word != '' and word[1:] != '':
        if word[0] in word[1:]:
            return False
        else:
            word = word[1:]
    return True

# Test code
print(isisogram(""))                 # True
print(isisogram("a"))                # True
print(isisogram("aa"))               # False
print(isisogram("and"))              # True
print(isisogram("hanyang"))          # False
print(isisogram("playground"))       # True
print(isisogram("uncopyrightables")) # True
