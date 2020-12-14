# index must be modulo'd by the length of each line, that way I can wrap around to the beginning
lineCounter = 0
position = 0
treeCounter = 0
with open("input3.txt", "r") as file:
    for line in file:
        line = line.strip()
        if lineCounter == 0 or lineCounter % 2 != 0:
            lineCounter += 1
            continue
        position += 1
        if line[position%len(line)] == '#':
            treeCounter += 1

        lineCounter += 1

print(treeCounter)


