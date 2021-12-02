seatList = []
newSeatList = []
counter = 0
adjacentCounter = 0
occupiedCount = 0
changed = True
# up, down, left, right, bottomright, bottomleft, topleft, topright
dir = [[0, 1], [0, -1], [-1, 0], [1, 0], [1, 1], [-1, 1], [-1, -1], [1, -1]]


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
                    if 95 > i + d[0] >= 0 and len(seatList[i]) > j + d[1] >= 0:
                        if seatList[i+d[0]][j+d[1]] == "#":
                            break
                    adjacentCounter += 1
                if adjacentCounter == 8:
                    newSeatList[i].append("#")
                    changed = True
                else:
                    newSeatList[i].append("L")

            elif seatList[i][j] == "#":
                for d in dir:
                    if 95 > i + d[0] >= 0 and len(seatList[i]) > j + d[1] >= 0:
                        if seatList[i+d[0]][j+d[1]] == "#":
                            adjacentCounter += 1
                if adjacentCounter >= 4:
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