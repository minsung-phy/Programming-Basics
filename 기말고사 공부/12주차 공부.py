# random 함수 
import random

## 1. random.random() : 0.0 <= x < 1.0의 실수(float)를 반환 
x = random.random()
print(x) # 0.0 ~ 0.99999999...

## 2. random.uniform(a, b) : a <= x <= b의 실수(float)를 반환
x = random.uniform(10, 20)
print(x) # 10.00000 <= x <= 20.00000

## 3. randint(a, b) : a <= N <= b의 정수(int)를 반환, = randrange(a, b+1)
x = random.randint(10, 20)
print(x) # 10 <= x <= 20

## 4. randrange(a, b) : a <= x < b의 정수(int)를 반환
##    randrange(b) : 0 <= x < b의 정수(int)를 반환
x1 = random.randrange(10, 20)
print(x1) # 10 <= x < 20
x2 = random.randrange(20)
print(x2) # 0 <= x < 20

## 5. random.choice(seq)
## choice 함수는 매개변수로 seq 타입을 받는다. 시퀀스 데이터 타입은 문자열, 튜플, range, 리스트 타입들을 말한다.
## 시퀀스 함수는 인자로 받은 리스트, 튜플, 문자열, range에서 무작위로 하나의 원소를 뽑습니다.
## 만약 비어있는 시퀀스 타입의 객체를 인자로 넣는다면 (ex. 리스트가 비어있다면) indexerror의 예외가 발생한다. <indexerror: 시퀀스의 인덱스가 범위를 벗어났을때 발생하는 에러>
x1 = random.choice("BlockDMask")
print(x1) # "BlockDMask" 문자열 중 랜덤한 문자를 반환
try:
    x2 = random.choice("")
    print(x2) # indexerror 발생
except IndexError:
    print("IndexError")

## 6. random.sample(seq or set, N)
## 첫번째 매개 변수로 시퀀스 데이터 타입(튜플, 문자열, range, 리스트) 또는 set 타입(집합)을 받을 수 있다.
## 두번째 매개 변수로는 랜덤하게 뽑을 인자의 개수이다.
## sample 함수는 첫번째 인자로 받은 시퀀스데이터 or set에서 N개의 랜덤하고, unique(겹치지 않는 요소를 반환)하고, 순서상관없이 인자를 뽑아서 리스트로 만들어서 반환해준다.
## 두번째 매개 변수 N이 seq, set의 인자의 개수를 넘어갈때 valueError가 발생한다.
arr1 = "abc"
print(random.sample(arr1, 2)) # ['a','b'] or ['b','c'] or ['c','a'] 순서는 바뀔 수 있음
arr2 = "ccc"
try:
    print(random.sample(arr2, 10)) # ValueError 발생
except ValueError:
    print("ValueError")
arr3 = "ccc"
print(random.sample(arr3, 3)) # ['c','c','c'] 반환

## 7. random.shuffle(seq) : 데이터의 순서를 무작위로 랜덤하게 바꾸어 주는 함수
## 매개변수 x에는 시퀀스 데이터 타입이 들어가게 된다. 하지만 내부의 값을 무작위로 바꿔야 하기 때문에 내부 인자를 변경할 수 있는 리스트만 가능하게 된다. (문자열, 튜플 및 range(a,b)는 불가능)
## random.shuffle(리스트)의 반환은 없고, 인자로 들어온 리스트 내부의 데이터를 무작위로 섞습니다.
arr = [1,2,3,4,5,6,7,8,9,10]
print(arr) # [1,2,3,4,5,6,7,8,9,10]
random.shuffle(arr)
print(arr) # 무작위로 변경됨

# input 함수 사용해보기
## word = input("단어를 입력하세요 : ")
word = "abc"
def reverse(word):
    re_word = ""
    for i in word:
        re_word = i + re_word
    return re_word
print("당신이 입력한", word, "를 거울에 비추면", reverse(word), "가 됩니다.")

# 리스트 다뤄보기
words = ["love", "poem", "fire", "wind"]
print(words)
words.append("water")
print(words)
words.remove("love")
print(words)

# 파일에서 단어 읽어오기
f = open("/Users/minsung/Documents/2학년 1학기/프로그래밍기초/12주차/words_sample.txt", "r")
for word in f.readlines():
    print(word)

# 파일에서 단어 읽어오기 2
word = "good\n"
case1 = word[:len(word)]
print(case1)
case2 = word[:len(word)-1]
print(case2)
case3 = word.strip('\n') # 문자열 word의 양쪽 끝에서 문자열 \n를 모두 제거하고 리턴한다. 인수가 비어있으면, 빈칸을 모두 제거하고 리턴한다.
print(case3)
case4, _ = word.split(sep='\n') # 구분 문자열 sep을 중심으로 문자열 word를 분리하여 리스트로 모아 리턴한다. 인수가 비어있으면, 빈칸을 구분 문자열로 하여 분리한다.
print(case4)

# 파일에서 단어 읽어오기 3
def load_words(file):
    f = open(file, "r", encoding="UTF-8")
    words = []
    for word in f.readlines():
        words.append(word.strip('\n'))
    words.sort()
    return words

# 단어 선택하기
import random
def pick_a_word(words):
    n = len(words)
    index = random.randint(0, n - 1)
    return words[index]

# 중간 점검 1
def main():
    sorted_words = load_words("/Users/minsung/Documents/2학년 1학기/프로그래밍기초/12주차/words_sample.txt")
    picked_word = pick_a_word(sorted_words)
    print("당신을 위한 단어는", picked_word, "입니다.")

# random.sample
for _ in range(10):
    values = random.sample([1,2,3,4,5], 2)
    print(values)

for _ in range(10):
    values = random.sample("skating", 3)
    print(values)

for _ in range(10):
    values = random.sample("osteoporosis", 3)
    print(values)

# 문자열 가리기
def puncture_word(word, n):
    target = random.sample(word, n)
    result = ""
    for s in word:
        if s in target:
            result = result + "_"
        else:
            result = result + s
    return result, target

# 중간 점검 2
def main2():
    sorted_words = load_words("/Users/minsung/Documents/2학년 1학기/프로그래밍기초/12주차/words_sample.txt")
    picked_word = pick_a_word(sorted_words)
    quiz_word, punctures = puncture_word(picked_word, 3)
    print("당신을 위한 단어는", quiz_word, "입니다.")

# 문자열 채우기
def guess(picked_word, quiz_word, target):
    c = input("guess a character(a-z) : ")
    while not(len(c) == 1 and 97 <= ord(c) <= 122):
        c = input("guess a character(a-z) : ")
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
    
# 중간 점검 3
def main3():
    sorted_words = load_words("/Users/minsung/Documents/2학년 1학기/프로그래밍기초/12주차/words_sample.txt")
    picked_word = pick_a_word(sorted_words)
    quiz_word, target = puncture_word(picked_word, 3)
    while "_" in quiz_word:
        print(quiz_word)
        quiz_word, target = guess(picked_word, quiz_word, target)
    print(picked_word)
    print("축하합니다!")

# 과제 4: 완성하기
def wordgame():
    sorted_words = load_words("/Users/minsung/Documents/2학년 1학기/프로그래밍기초/12주차/words_sample.txt")
    picked_word = pick_a_word(sorted_words)
    level = input("Beginner=1, Intermediate=2, Advanced=3 : ")
    count = 0
    while level not in ["1","2","3"]:
        level = input("Beginner=1, Intermediate=2, Advanced=3 : ")
    if level == "1":
        n = len(picked_word) // 3
    elif level == "2":
        n = len(picked_word) // 2
    else:
        n = len(picked_word)
    quiz_word, target = puncture_word(picked_word, n)
    while "_" in quiz_word:
        print(quiz_word)
        quiz_word, target = guess(picked_word, quiz_word, target)
        print("남은 횟수", 5 - count)
        count += 1
        if count > 5:
            print("횟수를 초과하였습니다. 프로그램을 종료합니다.")
            break
    if count < 5:
        print(picked_word)
        print("축하합니다!")

# 연습 5.9 모음 일련번호 매기기
def vowel_numbering(word):
    number = 1
    newword = ""
    for c in word:
        if c in ['a','e','i','o','u','A','E','I','O','U']:
            newword += str(number)
            number += 1
        else:
            newword += c
    return newword

# Test code
print(vowel_numbering('Massachussettes'))

# 연습 5.11 부분 리스트
## 가. drop_before 함수
def drop_before(s, index):
    if s != [] and index > 0:
        return drop_before(s[1:], index-1)
    else:
        return s

def drop_before(s, index):
    while s != [] and index > 0:
        s, index = s[1:], index-1
    return s

## 나. take_before 함수
def take_before(s, index):
    if s != [] and index > 0:
        return [s[0]] + take_before(s[1:], index-1)
    else:
        return []
    
def take_before(s, index):
    def loop(s, index, n):
        if s != [] and index > 0:
            return loop(s[1:], index-1, n + [s[0]])
        else:
            return n
    return loop(s, index, [])

def take_before(s, index):
    n = []
    while s != [] and index > 0:
        s, index, n = s[1:], index-1, n + [s[0]]
    return n

# 다. sublist 함수    
def sublist(s, low, high):
    if low < 0: low = 0
    if high < 0: high = 0
    if low < high:
        return take_before((drop_before(s, low)), high-low)
    else:
        return []
    
# Test code
s = [1,2,3,4,5]
print(sublist(s,2,4))
print(sublist(s,0,0))
print(sublist(s,3,6))
print(sublist(s,-3,-2))