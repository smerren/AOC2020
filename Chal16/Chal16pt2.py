rules = []
newRules = []
ticket = []
nearbyTickets = []
counter = 0

with open("input16.txt", "r") as file:
    for line in file:
        line = line.strip()
        if line == "":
            counter+=1
        elif counter == 0:
            line = line.split(": ")[1].split(" or ")
            rules.append(line)
        elif counter == 1 and "your ticket:" not in line:
            line = line.split(",")
            ticket.append(line)
        elif counter == 2 and "nearby tickets:" not in line:
            line = line.split(",")
            nearbyTickets.append(line)

for i in rules:
    for j in i:
        newRules.append(list(range(int(j.split("-")[0]), int(j.split("-")[1])+1)))

flat_rules_list = [item for sublist in newRules for item in sublist]

falseTickets = []
for i in nearbyTickets:
    for j in i:
        if int(j) not in flat_rules_list:
            falseTickets.append(i)

for i in falseTickets:
    nearbyTickets.remove(i)

newRules = [newRules[i] + (newRules[i+1] if i+1 < len(newRules) else []) for i in range(0, len(newRules), 2)]
dic = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[], 10:[], 11:[], 12:[], 13:[], 14:[], 15:[], 16:[], 17:[], 18:[], 19:[]}

for i in range(len(nearbyTickets[0])):
    lst = []
    for j in nearbyTickets:
        lst.append(j[i])
    for k in newRules:
        check = all(int(item) in k for item in lst)
        if check:
            dic[newRules.index(k)].append(i)

for k in dic.values():
    for i in dic.values():
        if len(i) == 1:
            for j in dic.values():
                if list(dic.values()).index(i) != list(dic.values()).index(j):
                    if i[0] in j:
                        j.remove(i[0])

multiple = 1
for i in range(0, 6):
    multiple *= int(ticket[0][dic[i][0]])
print(multiple)