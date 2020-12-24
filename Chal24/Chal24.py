ll = [x for x in open('input24.txt').read().strip().split('\n')]
dir = [[-1, 1], [0, 1], [1, 0], [1, -1], [0, -1], [-1, 0]]

lst = []
for _ in range(3):
    if lst:
        for j in range(len(lst)):
            j = lst[j].split(" ")
            for i in dir:
                if str(int(j[0])+i[0]) + " " + str(int(j[1])+i[1]) in lst:
                    pass
                else:
                    lst.append(str(int(j[0])+i[0]) + " " + str(int(j[1])+i[1]))
    else:
        for i in dir:
            lst.append(str(0 + i[0]) + " " + str(0 + i[1]))

def generateDic(dic, lst):
    for i in lst:
        dic[i] = "white"

    for i in ll:
        lst = []
        x, y = 0,0
        for j in range(len(i)):
            if i[j] == "s":
                lst.append(i[j] + i[j+1])
            if i[j] == "n":
                lst.append(i[j] + i[j+1])
            if (i[j] == "e" or i[j] == "w") and i[j-1] != 's' and i[j-1] != 'n':
                lst.append(i[j])

        for i in lst:
            if i == "e":
                x += 1
            elif i == "w":
                x -= 1
            elif i == "nw":
                y -= 1
            elif i == "se":
                y += 1
            elif i == "ne":
                x += 1
                y -= 1
            elif i == "sw":
                x -= 1
                y += 1

        coordString = ""
        coordString += str(x) + " " + str(y)

        if coordString not in dic.keys():
            dic[coordString] = "black"
        elif dic[coordString] == "black":
            dic[coordString] = "white"
        elif dic[coordString] == "white":
            dic[coordString] = "black"

    return dic

def func(dic):
    dictlist = []

    for j in dic.keys():
        white = 0
        black = 0
        for i in dir:
            coord = j.split(" ")
            newCoordString = str(int(coord[0])+i[0]) + " " + str(int(coord[1])+i[1])
            if newCoordString not in dic.keys():
                newblack=0
                for k in dir:
                    secondcoord = newCoordString.split(" ")
                    secondCoordString = str(int(secondcoord[0])+k[0]) + " " + str(int(secondcoord[1])+k[1])
                    if secondCoordString in dic.keys():
                        if dic[secondCoordString] == "black":
                            newblack+=1
                if newblack == 2:
                    dictlist.append([newCoordString, "black"])
                else:
                    dictlist.append([newCoordString, "white"])
            elif dic[newCoordString] == "black":
                black+=1
            elif dic[newCoordString] == "white":
                white+=1

        if dic[j] == "black":
            if black == 0 or black > 2:
                dictlist.append([j, "white"])
        elif dic[j] == "white":
            if black == 2:
                dictlist.append([j, "black"])

    for i in dictlist:
        dic[i[0]] = i[1]

    return dic

def main():
    dic = generateDic({}, lst)
    print("part 1: " + str(list(dic.values()).count('black')))
    for _ in range(100):
        dic = func(dic)
    print("part 2: " + str(list(dic.values()).count('black')))

main()