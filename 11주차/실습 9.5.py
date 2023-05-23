def load_members():
    file = open("/Users/minsung/Documents/2학년 1학기/프로그래밍기초/11주차/members.csv", "r")
    members = {}
    for line in file:
        name, passwd, tries, wins, chips = line.strip('\n').split(',')
        members[name] = (passwd, int(tries), float(wins), int(chips))
    file.close()
    return members

def store_members(members):
    file = open("/Users/minsung/Documents/2학년 1학기/프로그래밍기초/11주차/members.csv", "w")
    names = members.keys()
    for name in names:
        passwd, tries, wins, chips = members[name]
        line = name + ',' + passwd + ','+ str(tries) + ',' + str(wins) + ',' + str(chips) + '\n'
        file.write(line)
    file.close()

members = {"lms": ("min9", 10, 9, 17)}

store_members(members)
print(load_members())