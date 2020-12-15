spokenList = [int(line) for line in open('input15.txt').read().strip().split(",")]
turnNumber = len(spokenList)

while len(spokenList) != 2020:
    if spokenList[-1] not in spokenList[:-1]:
        spokenList.append(0)
    else:
        lastSeen = max(l for l, v in enumerate(spokenList[:-1]) if v == spokenList[-1])
        spokenList.append(turnNumber - lastSeen-1)
    turnNumber+=1

print(spokenList[-1])