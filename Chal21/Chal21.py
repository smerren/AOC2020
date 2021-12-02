import collections
dic = {}
newdic = {}
lineList = []
allergensList = []
ingList = []

def generateLists():
    with open("input21.txt", "r") as file:
        for l in file:
            l = l.strip()
            l = l.split("contains")
            l = [l[0].strip(" ("), l[1][1:].strip(")")]
            allergens = l[1].split(", ")
            lineList.append(l[0])
            for i in allergens:
                if i not in allergensList:
                    allergensList.append(i)
                if i not in dic.keys():
                    dic[i] = []
                dic[i].append(l[0])


    for i in allergensList:
        for j in dic[i]:
            j = j.split(" ")
            for k in j:
                if not k in ingList:
                    ingList.append(k)

    for i in dic.keys():
        for k in ingList:
            sumOfK = 0
            for j in dic[i]:
                j = j.split(" ")
                if k in j:
                    sumOfK += 1
                    continue
            if len(dic[i]) == sumOfK:
                if i not in newdic.keys():
                    newdic[i] = []
                newdic[i].append(k)

    for _ in newdic.values():
        for i in newdic.values():
            if len(i) == 1:
                for j in newdic.values():
                    if list(newdic.values()).index(i) != list(newdic.values()).index(j):
                        if i[0] in j:
                            j.remove(i[0])
def part1():
    s = 0
    for i in lineList:
        line = i.split(" ")
        for j in newdic.values():
            if j[0] in line:
                line.remove(j[0])
                continue
        s += len(line)
    print("part 1: " + str(s))

def part2():
    allergenString = ""
    od = collections.OrderedDict(sorted(newdic.items()))
    for i in od.values():
        allergenString += i[0] + ","
    allergenString = allergenString[:-1]
    print("part 2: " + allergenString)

generateLists()
part1()
part2()
