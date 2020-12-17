GOL3D = []
from itertools import product
dir = [list(x) for x in list(product(range(-1, 2), repeat = 3))]
dir.remove([0,0,0])
z = 1

def createState(input):
    with open(input, "r") as file:
        for line in file:
            line = line.strip()
            for i in range(z+2):
                GOL3D.append([['.' for _ in range(len(line)+2)] for _ in range(len(line)+2)])
            break
    with open(input, "r") as file:
        counter = 0
        for line in file:
            counter += 1
            line = line.strip()
            line = [char for char in line]
            for i in range(1, len(line)+1):
                GOL3D[len(GOL3D)//2][counter][i] = line[i-1]

def updateStateList(list):
    for layer in list:
        layer.insert(0, ['.' for _ in range(len(layer))])
        layer.insert(len(list[0]), ['.' for _ in range(len(layer)-1)])

    for layer in list:
        for row in layer:
            row.insert(0, '.')
            row.insert(len(row), '.')

    list.insert(0, [['.' for _ in range(len(newList[0]))] for _ in range(len(newList[0]))])
    list.insert(len(list), [['.' for _ in range(len(newList[0]))] for _ in range(len(newList[0]))])
    return list

z = createState("input17.txt")

cycle = 0
# TODO: DO THIS EVERY CYCLE
while cycle < 6:
    newList = []
    for i in range(len(GOL3D)):
        newList.append([])
        for j in range(len(GOL3D[i])):
            newList[i].append([])
            for k in range(len(GOL3D[i][j])):
                newList[i][j].append('.')
                activeCounter = 0
                inactiveCounter = 0
                for d in dir:
                    if 0 <= i+d[0] < len(GOL3D):
                        if 0 <= j+d[1] < len(GOL3D[i]):
                            if 0 <= k + d[2] < len(GOL3D[i][j]):
                                if GOL3D[i+d[0]][j+d[1]][k+d[2]] == "#":
                                    activeCounter += 1
                                else:
                                    inactiveCounter += 1

                if GOL3D[i][j][k] == "#":
                    if activeCounter < 2 or activeCounter > 3:
                        newList[i][j][k] = '.'
                    else:
                        newList[i][j][k] = '#'
                elif GOL3D[i][j][k] == ".":
                    if activeCounter == 3:
                        newList[i][j][k] = '#'
                    else:
                        newList[i][j][k] = '.'

    GOL3D = updateStateList(newList)
    cycle += 1

activeCounter = 0
for i in GOL3D:
    for j in i:
        for k in j:
            if k == "#":
                activeCounter += 1
print(activeCounter)