GOL3D = []
from itertools import product
dir = [list(x) for x in list(product(range(-1, 2), repeat = 4))]
dir.remove([0,0,0,0])

def createState(input):
    with open(input, "r") as file:
        for line in file:
            line = line.strip()
            for i in range(3):
                GOL3D.append([[['.' for _ in range(len(line)+2)] for _ in range(len(line)+2)] for _ in range(len(line)+2)])
            break
    with open(input, "r") as file:
        counter = 0
        for line in file:
            counter += 1
            line = line.strip()
            line = [char for char in line]
            for i in range(1, len(line)+1):
                GOL3D[len(GOL3D)//2][len(GOL3D)//2][counter][i] = line[i-1]

def updateStateList(list):
    for w in list:
        for layer in w:
            layer.insert(0, ['.' for _ in range(len(layer))])
            layer.insert(len(layer), ['.' for _ in range(len(layer)-1)])

    for w in list:
        for layer in w:
            for row in layer:
                row.insert(0, '.')
                row.insert(len(row), '.')

    for w in list:
        w.insert(0, [['.' for _ in range(len(newList[0][0]))] for _ in range(len(newList[0][0]))])
        w.insert(len(w), [['.' for _ in range(len(newList[0][0]))] for _ in range(len(newList[0][0]))])

    list.insert(0, [[['.' for _ in range(len(list[0][0][0]))] for _ in range(len(list[0][0][0]))] for _ in range(len(list[0][0][0]))])
    list.insert(len(list), [[['.' for _ in range(len(list[0][0][0]))] for _ in range(len(list[0][0][0]))] for _ in range(len(list[0][0][0]))])
    return list

createState("input17.txt")

cycle = 0
# TODO: DO THIS EVERY CYCLE
while cycle < 6:
    newList = []
    for i in range(len(GOL3D)):
        newList.append([])
        for j in range(len(GOL3D[i])):
            newList[i].append([])
            for k in range(len(GOL3D[i][j])):
                newList[i][j].append([])
                for w in range(len(GOL3D[i][j][k])):
                    newList[i][j][k].append('.')
                    activeCounter = 0
                    inactiveCounter = 0
                    for d in dir:
                        if 0 <= i+d[0] < len(GOL3D):
                            if 0 <= j+d[1] < len(GOL3D[i]):
                                if 0 <= k + d[2] < len(GOL3D[i][j]):
                                    if 0 <= w + d[3] < len(GOL3D[i][j][k]):
                                        if GOL3D[i+d[0]][j+d[1]][k+d[2]][w+d[3]] == "#":
                                            activeCounter += 1
                                        else:
                                            inactiveCounter += 1


                    if GOL3D[i][j][k][w] == "#":
                        if activeCounter < 2 or activeCounter > 3:
                            newList[i][j][k][w] = '.'
                        else:
                            newList[i][j][k][w] = '#'
                    elif GOL3D[i][j][k][w] == ".":
                        if activeCounter == 3:
                            newList[i][j][k][w] = '#'
                        else:
                            newList[i][j][k][w] = '.'

    GOL3D = updateStateList(newList)
    cycle += 1

activeCounter = 0
for i in GOL3D:
    for j in i:
        for k in j:
            for w in k:
                if w == "#":
                    activeCounter += 1
print(activeCounter)