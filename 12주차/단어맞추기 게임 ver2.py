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

def guess(picked_word, quiz_word, target, lim):
    while lim > 0 and '_' in quiz_word:
        print(quiz_word)
        print("남은 횟수:", lim)
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
        else:
            lim -= 1
    if '_' not in quiz_word:
        print(picked_word)
        print("축하합니다!")
    else:
        print("실패하였습니다. 정답은 {}입니다.".format(picked_word))

def main():
    sorted_words = load_words("/Users/minsung/Documents/2학년 1학기/프로그래밍기초/12주차/words_sample.txt")
    picked_word = pick_a_word(sorted_words)
    print("Enter your level.")
    level = input("Beginner=1, Intermediate=2, Advanced=3 : ")
    while level not in ("1","2","3"):
        level = input("Beginner=1, Intermediate=2, Advanced=3 : ")
    if level == "1":
        quiz_word, target = puncture_word(picked_word, int(len(picked_word)/3))
        lim = 10
    elif level == "2":
        quiz_word, target = puncture_word(picked_word, int(len(picked_word)/2))
        lim = 7 
    else:
        quiz_word, target = puncture_word(picked_word, int(len(picked_word)))
        lim = 5
    guess(picked_word, quiz_word, target, lim)

main()
