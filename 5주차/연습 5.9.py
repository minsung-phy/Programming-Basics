def vowel_numbering(word):
    number = 1
    newword = ''
    for c in word:
        if c in ['a','e','i','o','u','A','E','I','O','U']:
            newword = newword + str(number)
            number = number + 1
        else:
            newword = newword + c
    return newword

# Test code
print(vowel_numbering('Massachussettes')) # 'M1ss2ch3ss4tt5s'