letters = []
lettersOfFirstInGroup = []
counter = 0
groupCount = 0
groupStart = True

with open("input6.txt", "r") as file:
    for line in file:
        line = line.strip()
        if line == "":
            for char in lettersOfFirstInGroup:
                if letters.count(char) == groupCount:
                    counter += 1
            letters = []
            lettersOfFirstInGroup = []
            groupStart = True
            groupCount = 0
            continue

        groupCount += 1

        if groupStart == True:
            for char in line:
                lettersOfFirstInGroup.append(char)
                letters.append(char)
            groupStart = False
            continue

        for char in line:
            letters.append(char)

print(counter)