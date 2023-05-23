def login(members):
    username = input("Enter your name: (4 letters max) ")
    while len(username) > 4:
        username = input("Enter your name: (4 letters max) ")
    trypasswd = input("Enter your password: ")
    if username in members.keys():
        if trypasswd == members[username][0]():
            tries = members[username][1]
            wins = members[username][2]
            print("You played", tries, "games and won", wins, "of them")
            wpercent = wins / tries * 100 if tries > 0 else 0
            print("Your all-time winning percentage is", "{0:.1f}".format(wpercent), "%")
            chips = members[username][3]
            if chips > 0:
                print("you have", chips, "chips.")
            else:
                print("you owe", -chips, "chips.")
            return username, tries, wins, chips, members
        else:
            return login(members)
    else:
        members[username] = (trypasswd, 0, 0, 0)
        return username, 0, 0, 0, members