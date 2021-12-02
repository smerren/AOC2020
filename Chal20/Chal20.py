pog = []
idList = []
with open("input20.txt", "r") as f:
    lst = []
    for line in f:
        line = line.strip()
        if line == "":
            pog.append(lst)
            lst = []
        elif "Tile" in line:
            idList.append(line.split(" ")[1].strip(":"))
        else:
            lst.append(list(line))

dic = {}
for i in pog:
    sidelist = []
    leftSide = [list(row) for row in zip(*reversed(i))]
    bottom = [list(row) for row in zip(*reversed(leftSide))]
    rightSide = [list(row) for row in zip(*reversed(bottom))]
    Normal = [list(row) for row in zip(*reversed(rightSide))]
    sidelist.append(list(reversed(leftSide[0])))
    sidelist.append(list(reversed(bottom[0])))
    sidelist.append(list(reversed(rightSide[0])))
    sidelist.append(list(reversed(Normal[0])))

    for j in pog:
        if i == j:
            continue
        sidelistj = []
        leftSidej = [list(row) for row in zip(*reversed(j))]
        bottomj = [list(row) for row in zip(*reversed(leftSidej))]
        rightSidej = [list(row) for row in zip(*reversed(bottomj))]
        Normalj = [list(row) for row in zip(*reversed(rightSidej))]
        sidelistj.append(leftSidej[-1])
        sidelistj.append(list(reversed(leftSidej[-1])))
        sidelistj.append(bottomj[-1])
        sidelistj.append(list(reversed(bottomj[-1])))
        sidelistj.append(rightSidej[-1])
        sidelistj.append(list(reversed(rightSidej[-1])))
        sidelistj.append(Normalj[-1])
        sidelistj.append(list(reversed(Normalj[-1])))

        if idList[pog.index(i)] not in dic.keys():
            dic[idList[pog.index(i)]] = []

        for k in sidelist:
            if k in sidelistj:
                if idList[pog.index(j)] not in dic[idList[pog.index(i)]]:
                    dic[idList[pog.index(i)]].append(idList[pog.index(j)])
mul = 1
for i in idList:
    if len(dic[i]) == 2:
        mul *= [int(k) for k,v in dic.items() if v == dic[i]][0]

print(mul)
