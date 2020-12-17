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

counter=0
for i in nearbyTickets:
    for j in i:
        if int(j) not in flat_rules_list:
            counter+=int(j)

print(counter)