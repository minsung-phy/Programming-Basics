def load_members():
    file = open("/Users/minsung/Documents/2학년 1학기/프로그래밍기초/11주차/members.csv", "r")
    members = {}
    for line in file:
        name, passwd, tries, wins, chips = line.strip('\n').split(',')
        members[name] = (passwd, int(tries), float(wins), int(chips))
    file.close()
    return members

print(load_members())