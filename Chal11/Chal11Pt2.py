seatList = []
newSeatList = []
counter = 0
adjacentCounter = 0
occupiedCount = 0
changed = True
dir = [[0, 1], [0, -1], [-1, 0], [1, 0], [1, 1], [-1, 1], [-1, -1], [1, -1]]

def recursiveWalking(dirx, diry, dir):
    if 95 > dirx >= 0 and len(seatList[i]) > diry >= 0:
        if seatList[dirx][diry] == "#":
            return True
        elif seatList[dirx][diry] == "L":
            return False
        else:
            return recursiveWalking(dirx+dir[0], diry+dir[1], dir)
    return False

for i in range(95):
    seatList.append([])
    newSeatList.append([])

with open("input11.txt", "r") as file:
    for line in file:
        line = line.strip()
        for i in line:
            seatList[counter].append(i)
        counter += 1

while changed:
    changed = False
    for i in range(len(seatList)):
        for j in range(len(seatList[i])):
            if seatList[i][j] == "L":
                for d in dir:
                    found = recursiveWalking(i+d[0], j+d[1], d)
                    if found:
                        break
                    adjacentCounter += 1
                if adjacentCounter == 8:
                    newSeatList[i].append("#")
                    changed = True
                else:
                    newSeatList[i].append("L")

            elif seatList[i][j] == "#":
                for d in dir:
                    found = recursiveWalking(i + d[0], j + d[1], d)
                    if found:
                        adjacentCounter += 1
                if adjacentCounter >= 5:
                    newSeatList[i].append("L")
                    changed = True
                else:
                    newSeatList[i].append("#")

            elif seatList[i][j] == ".":
                newSeatList[i].append(".")

            adjacentCounter = 0
    if not changed:
        break

    for i in range(len(newSeatList)):
        seatList[i] = newSeatList[i]
        newSeatList[i] = []

for i in seatList:
    occupiedCount += i.count("#")

print(occupiedCount)