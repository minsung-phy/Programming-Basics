import random

def load_words(file):
    f = open(file, "r", encoding="UTF-8")
    words = []
    for word in f.readlines():
        words.append(word.strip('\n'))
    words.sort()
    return words

def pick_a_word(words):
    n = len(words)
    index = random.randint(0, n-1)
    return words[index]

def puncture_word(word, n):
    target = random.sample(word, n)
    result = ""
    for s in word:
        if s in target:
            result = result + "_"
        else:
            result = result + s
    return result, target

def guess(picked_word, quiz_word, target):
    c = input("guess a hidden character : ")
    while not(len(c) == 1 and 97 <= ord(c) <= 122):
        c = input("guess a hidden character : ")
    if c in target:
        target.remove(c)
        quiz_word = ""
        for s in picked_word:
            if s in target:
                quiz_word += "_"
            else:
                quiz_word += s
        return quiz_word, target
    else:
        return quiz_word, target

def main():
    sorted_words = load_words("/Users/minsung/Documents/2학년 1학기/프로그래밍기초/12주차/words_sample.txt")
    picked_word = pick_a_word(sorted_words)
    quiz_word, target = puncture_word(picked_word, 3)
    while '_' in quiz_word:
        print(quiz_word)
        quiz_word, target = guess(picked_word, quiz_word, target)
    print(picked_word)
    print("축하합니다!")

main()