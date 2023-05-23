def show_top5(members):
    print("---")
    sorted_members = sorted(members.items(), key=lambda x: x[1][3], reverse=True)
    print("All-time Top 5 based on the number of chips eaerned")
    rank = 1
    for members in sorted_members[:5]:
        chips = members[1][3]
        if chips <= 0:
            break
    print(rank, ".", members[0], ":", chips)
    rank += 1

members = {"doh": ("sid73", 993, 550, 35), "didi": ("edd484", 130, 55, 10), "hy": ("er878re", 35, 18, 2), "dr": ("qwert", 18, 8, 0), "who": ("poiuy", 34, 18, 0)}
print(show_top5(members))