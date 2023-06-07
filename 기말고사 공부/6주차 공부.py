# 실습 6.1 논리 연산자로 흐름 제어
def bin_search_OX(ss, x):
    while ss != []:
        mid = len(ss) // 2
        if x == ss[mid]:
            return True
        elif x < ss[mid]:
            ss = ss[:mid]
        else:
            ss = ss[mid+1:]
    return False

def bin_search_OX(ss, x):
    mid = len(ss) // 2
    return ss != [] and (x == ss[mid] or x < ss[mid] and bin_search_OX(ss[:mid], x) or bin_search_OX(ss[mid+1:], x))

# 텍스트 파일 처리

# 파일 열기와 닫기:
# 파일을 대상으로 읽거나 쓰려면 먼저 파일을 용도에 맞추어 열어야 한다. 파일은 open 함수로 연다. 예를 들어 프로그램 파일과 같은 폴더에 위치한 input.txt 파일을 일기용으로 열고 싶으면 다음과 같이 쓴다.
# t = open("input.txt", "r")
# 여기서 open 함수 호출의 첫째 인수는 열고 싶은 파일 이름이다. 대상 파일이 다른 폴더에 잇는 경우에는 파일 경로도 함께 명시해야 한다.
# 둘째 인수인 "r"은 접근모드를 나타내는데, 파일을 읽을 (read) 용도로 열어달라는 요청이다. 
# open 함수로 열어준 input.txt 파일은 변수 t로 지정하였으므로, 이 변수를 통하여 연 파일에 접근 할 수 있다. 
# 파일을 읽기용으로 열면, 그 파일에 기록되어 있는 문자열을 맨 앞에서부터 순서대로 읽을 수 있고, 파일이 열려있는 동안 어디까지 읽었는지 기억해준다.
# 열었던 파일은 사용 후 반드시 다음과 같은 형식으로 닫아야 한다.
# t.close()
# 파일을 닫지 않으면 다른 프로그램의 접근 가능성을 열어두는 셈이 되므로, 보안을 위하여 한 번 연 파일은 사용후 반드시 닫도록 해야한다.
# 접근모드 / 의미
# "r" / 파일에서 읽음 (파일이 없으면 오류)
# "w" / 파일에 씀 (파일이 있으면 지우고 새로 씀, 없으면 새로 만듦)
# "x" / 새로 생성한 파일에 씀 (파일이 있으면 오류)
# "a" / 파일의 뒤에 이어서 씀 (파일이 없으면 새로 만듦)
# "r+" / 파일에서 읽고 씀 (파일이 없으면 오류)
# "w+" / 파일에 쓰고 읽음 (파일이 있으면 지우로 새로 씀, 없으면 새로 만듦)
# "a+" / 파일의 뒤에 이어서 쓰고 읽음 (파일이 없으면 새로 만듦)

# 텍스트 파일에서 문자열 읽기:
# input.txt에서 첫 n개의 문자를 읽어오려면, 그 파일을 읽을 용도로 열고 read(n) 메소드를 호출하면 된다. 
# 예를 들어 input.txt 파일에서 첫 문자 하나만 읽어오려면 다음과 같이 한다.
t = open("/Users/minsung/Documents/2학년 1학기/프로그래밍기초/기말고사 공부/input.txt", "r")
print(t.read(1))
# 이어서 9자를 더 읽어서 프린트하고 싶으면 계속해서 다음과 같이 한다.
print(t.read(9))
# 읽을 때 어디까지 읽었는지 항상 기억하기 때문에, 추후에 읽으면 기억해 둔 곳에서부터 읽는다. 
# 파일 끝에 도달하면 그 이후에 읽은 결과는 빈 문자열이 된다. 처음부터 다시 읽고 싶으면 다음과 같이 해당 파일을 닫고 다시 열어야 한다.
t.close()
t = open("/Users/minsung/Documents/2학년 1학기/프로그래밍기초/기말고사 공부/input.txt", "r")
# 다음과 같이 읽을 문자의 개수를 명시하지 않으면 파일에서 남은 문자열 전체를 끝까지 다 읽어버린다.
print(t.read())
# 바로 전에 파일 t를 다시 열었기 때문에, 파일을 처음부터 끝까지 모두 읽어서 실행창에 프린트했다.
t.close()

# 파일에서 현재 읽고 있는 줄에서만 n개의 문자를 읽어오려면 readline(n) 메소드를 쓴다.
t = open("/Users/minsung/Documents/2학년 1학기/프로그래밍기초/기말고사 공부/input.txt", "r")
print(t.readline(1))
print(t.readline(9))
t.close()
# 이 사례만 보면 read(n)과 별 차이가 없어 보인다. 그러나 차이가 있다. 
# read(n)은 파일 전체에서 문자 n개를 읽어오는 반면, readline(n)은 현재 줄에서만 문자 n개를 읽어오고 다음 줄로 절대 넘어가지 않는다.
# readline()은 파일을 한 줄 단위로 읽을 때 편리하게 사용할 수 있다. 예를 들어 input.txt 파일을 한 줄씩 읽어서 프린트하려면 다음과 같이 하면 된다.
t = open("/Users/minsung/Documents/2학년 1학기/프로그래밍기초/기말고사 공부/input.txt", "r")
print(t.readline())
print(t.readline())
print(t.readline())
t.close()

# 텍스트 파일에 문자열 쓰기:
# 텍스트 파일에 쓸 때도 쓰기 전에 해당 파일을 먼저 열어야 한다. output.txt 파일에 문자열을 쓰고 싶으면 다음과 같이 "w"모드로 파일을 열어야 한다.
t = open("/Users/minsung/Documents/2학년 1학기/프로그래밍기초/기말고사 공부/output.txt", "w")
# 그러면 내용이 비어있는 output.txt 파일이 새로 생겨나며 파일에 문자열을 써주기를 기다린다. 만약 같은 이름의 파일이 이미 있다면, 그 파일을 지우고 내용이 빈 새로운 파일로 대체한다.
# 기존 파일을 의도치 않게 지워버리는 사고를 방지하고 싶으면 "x"모드를 사용한다. 이 모드는 같은 이름의 파일이 있으면, 쓰는 대신 오류가 발생한다.

# 파일 t에 문자열을 쓰려면 write() 메소드를 다음과 같이 호출한다.
t.write("새 나라의 어린이는 일찍 일어납니다\n")
# 그런데 write() 메소드는 쓰는 문자열의 맨 끝에 줄바꿈 문자를 넣지 않는다. 따라서 줄을 바꾸고 싶으면 원하는 위치에 "\n"을 명시해야 한다.
t.write("잠꾸러기 없는 나라\n")
t.write("우리나라 좋은 나라\n")
t.close()
# 위에서 본 input.txt 파일과 똑같은 내용이 들어있는 output.txt를 위와 같이 만들 수 있다.

# 파일 메소드 요약:
# 메소드 / 실행의미
# close() / 파일을 닫는다. 일단 닫힌 파일은 다시 열기 전에는 읽거나 쓸 수 없다.
# read(n) / 파일의 현재 위치에서 문자 n개를 읽어서 문자열로 리턴한다.
# read() / 파일의 현재 위치에서 파일의 끝까지 모두 문자열로 리턴한다.
# readline(n) / 파일의 현재 위치에서 그 줄의 문자 n개를 읽어서 문자열로 리턴한다.
# readline() / 파일의 현재 위치에서 그 줄의 끝까지 모두 문자열로 리턴한다.
# readlines() / 파일의 현재 위치에서 한 줄씩 끝가지 읽어서 줄의 리스트로 리턴한다.
# write(s) / 문자열 s를 파일의 현재 위치에 쓴다.
# writelines(ss) / 문자열 리스트 ss에 있는 문자열을 모두 파일의 현재 위치에 쓴다.

# 문자열 검색

# 문자열 메소드 : 문자열 검색에 유용하게 사용할 수 있는 것
# 문자열 메소드 / 실행 의미
# str.find(sub) / str에서 맨 앞에 나타나는 sub의 시작 인덱스를 리턴, 없으면 -1을 리턴
# str.index(sub) / str에서 맨 앞에 나타나는 sub의 시작 인덱스를 리턴, 없으면 ValueError 오류 발생
# str.rfind(sub) / str에서 맨 뒤에 나타나는 sub의 시작 인덱스를 리턴, 없으면 -1을 리턴
# str.startswith(prefix) / str이 prefix로 시작하면 True를 리턴, 그렇지 않으면 False를 리턴
# str.endswith(suffix) / str이 suffix로 끝나면 True를 리턴, 그렇지 않으면 False를 리턴
# find는 문자열 전용이고, index는 모든 시퀀스에 공통으로 사용한다.

text = "Your time is limited, so don't waste it living someone else's life."
print(text.find("me"))
print(text.find("li"))
print(text.find("live"))
print(text.rfind("me"))
print(text.rfind("li"))

text = "Individual Freedom"
print(text.startswith("I"))
print(text.startswith("Indian"))
print(text.endswith("dom"))
print(text.endswith("Free"))

# 대상 문자열의 검색 범위를 지정하여 검색 대상을 제한할 수도 있다. 검색 범위의 시작 인덱스와 끝 인덱스를 문자열 조각내기와 동일한 요령으로 인수로 추가하면 된다.
text = "Your time is limited, so don't waste it living someone else's life."
print(text.find("me"))
print(text.find("me", 8))
print(text.find("me", 8, 49))

# 처음 나타나는 문자열 하나만 찾기:
# 파일이름 filename과 찾으려는 문자열 x를 인수로 받아서 텍스트 파일에서 문자열 x가 처음 나타나는 위치 인덱스를 "result.txt"라는 이름의 파일에 쓰는 프로시저 find_1st를 만들어보자.
# 예를 들어 읽어올 텍스트 파일 이름이 "article.txt"이고 찾으려는 문자열이 "computer"이면, find_1st("article.txt", "computer")를 호출하고, 
# 문자열 "computer"가 텍스트 파일 "article.txt"에서 처음 나타난 인덱스를 "result.txt" 파일에 형식에 맞추어 쓴다. 
# 만약 없으면 "not found"를 "result.txt" 파일에 형식에 맞추어 쓴다.
def find_1st(filename, x):
    infile = open(filename, "r")
    outfile = open("/Users/minsung/Documents/2학년 1학기/프로그래밍기초/기말고사 공부/result.txt", "w")
    text = infile.read()
    position = text.find(x)
    if position == -1:
        outfile.write(x + " is not found.\n")
    else:
        outfile.write(x + " is at " + str(position) + " the 1st time.\n")
    outfile.close()
    infile.close()
    print("Done")

# 실습 6.2 find_1st 함수 테스트
find_1st("/Users/minsung/Documents/2학년 1학기/프로그래밍기초/기말고사 공부/article.txt", "computer")
find_1st("/Users/minsung/Documents/2학년 1학기/프로그래밍기초/기말고사 공부/article.txt", "Whole Earth")
find_1st("/Users/minsung/Documents/2학년 1학기/프로그래밍기초/기말고사 공부/article.txt", "Apple")
find_1st("/Users/minsung/Documents/2학년 1학기/프로그래밍기초/기말고사 공부/article.txt", "apple")

# 둘째로 나타나는 문자열 하나만 찾기
# 파일이름 filename과 찾으려는 문자열 x를 인수로 받아서 텍스트 파일에서 문자열 x가 둘째로 나타나는 위치 인덱스를 "result.txt"라는 이름의 파일에 쓰는 프로시저 find_2nd를 만들어보자.
# 예를 들어 읽어올 텍스트 파일 이름이 "article.txt"이고 찾으려는 문자열이 "computer"이면, find_2nd("article.txt", "computer")를 호출하고,
# 문자열 "computer"가 텍스트 파일 "article.txt"에서 둘쨰로 나타난 인덱스를 "result.txt" 파일에 형식에 맞추어 쓴다. 
# 만약 없거나 한 번만 나타나면 "not found"를 "result.txt" 파일에 형식에 맞추어 쓴다.
def find_2nd(filename, x):
    infile = open(filename, "r")
    outfile = open("/Users/minsung/Documents/2학년 1학기/프로그래밍기초/기말고사 공부/result.txt", "w")
    text = infile.read()
    position = text.find(x)
    position = text.find(x, position+1)
    if position == -1:
        outfile.write(x + " is not found.\n")
    else:
        outfile.write(x + " is at " + str(position) + " the 2nd time.\n")
    outfile.close()
    infile.close()
    print("Done")

# 실습 6.3 find_2nd 함수 테스트
find_2nd("/Users/minsung/Documents/2학년 1학기/프로그래밍기초/기말고사 공부/article.txt", "computer")
find_2nd("/Users/minsung/Documents/2학년 1학기/프로그래밍기초/기말고사 공부/article.txt", "Whole Earth")
find_2nd("/Users/minsung/Documents/2학년 1학기/프로그래밍기초/기말고사 공부/article.txt", "Apple")
find_2nd("/Users/minsung/Documents/2학년 1학기/프로그래밍기초/기말고사 공부/article.txt", "apple")

# 실습 6.4 마지막 문자열 하나만 찾기
def find_last(filename, x):
    infile = open(filename, "r")
    outfile = open("/Users/minsung/Documents/2학년 1학기/프로그래밍기초/기말고사 공부/result.txt", "w")
    text = infile.read()
    found_most_recent = -1
    position = text.find(x)
    while position != -1:
        found_most_recent = position
        position = text.find(x, position+1)
    if found_most_recent == -1:
        outfile.write(x + " is not found.\n")
    else:
        outfile.write(x + " is at " + str(found_most_recent) + " the last time.\n")
    outfile.close()
    infile.close()
    print("Done")

find_last("article.txt", 'computer')   

# 실습 6.5 모두 찾기
def find_all(filename, x):
    infile = open(filename, "r")
    outfile = open("/Users/minsung/Documents/2학년 1학기/프로그래밍기초/기말고사 공부/result.txt", "w")
    text = infile.read()
    position = text.find(x)
    if position == -1:
        outfile.write(x + " is not found.\n")
    while position != -1:
        outfile.write(x + " is at " + str(position) + " the time.\n")
        position = text.find(x, position+1)
    outfile.close()
    infile.close()
    print("Done")

find_all("/Users/minsung/Documents/2학년 1학기/프로그래밍기초/기말고사 공부/article.txt", 'computer')  

# 실습 6.6 모두 찾고, 찾은 개수 세기
def find_all_count(filename, x):
    infile = open(filename, "r")
    outfile = open("/Users/minsung/Documents/2학년 1학기/프로그래밍기초/기말고사 공부/result.txt", "w")
    text = infile.read()
    position = text.find(x)
    count = 0
    if position == -1:
        outfile.write(x + " is not found. | count: 0\n")
    while position != -1:
        count += 1
        outfile.write(x + " is at " + str(position) + " the time. | count: " + str(count) + "\n")
        position = text.find(x, position+1)
    outfile.close()
    infile.close()
    print("Done")

find_all_count("/Users/minsung/Documents/2학년 1학기/프로그래밍기초/기말고사 공부/article.txt", 'computer') 

# 실습 6.7 인용 문장 모두 찾기
def find_quotes_all(filename):
    infile = open(filename,"r")
    outfile = open("/Users/minsung/Documents/2학년 1학기/프로그래밍기초/기말고사 공부/result.txt","w")
    text = infile.read()
    index = text.find('"')
    while index != -1:
        index2 = text.find('"', index+1)
        outfile.write(text[index:index2+1] + "\n\n")
        index = text.find('"',index2+1)
    outfile.close()
    infile.close()
    print("Done")

# Test code 
find_quotes_all('/Users/minsung/Documents/2학년 1학기/프로그래밍기초/기말고사 공부/article.txt')

# 연습 6.5 아이소그램 확인
def isisogram(x):
    while x != "" and x[1:] != "":
        if x[0] in x[1:]:
            return False
        else:
            x = x[1:]
    return True

# 연습 6.6 아나그램 확인
def isanagram(word1, word2):
    while word1 != "":
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

def isanagram(word1, word2):
    while word1 != "":
        if word1[0] in word2:
            index = word2.find(word1[0])
            word1 = word1[1:]
            word2 = word2[:index] + word2[index+1:]
        else:
            return False
    return word2 == ''
