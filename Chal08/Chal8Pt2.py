instArray = []
counter = 0
acc = 0
loopCounter = 0
counterArray = []

with open("input8.txt", "r") as file:
    for line in file:
        line = line.strip()
        lineTemp = line.split(" ")
        instArray.append(lineTemp)

while True:
    if instArray[loopCounter][0] == "jmp":
        instArray[loopCounter][0] = "nop"
    elif instArray[loopCounter][0] == "nop":
        instArray[loopCounter][0] = "jmp"

    while True:
        if instArray[counter][0] == "nop":
            counter+=1

        elif instArray[counter][0] == "acc":
            acc += int(instArray[counter][1])
            counter += 1

        elif instArray[counter][0] == "jmp":
            counter += int(instArray[counter][1])

        if counter in counterArray:
            break
        else:
            counterArray.append(counter)

        if counter >= len(instArray):
            break

    if counter >= len(instArray):
        break
    else:
        counter = 0
        counterArray = []
        acc = 0
        if instArray[loopCounter][0] == "jmp":
            instArray[loopCounter][0] = "nop"

        elif instArray[loopCounter][0] == "nop":
            instArray[loopCounter][0] = "jmp"

        loopCounter += 1

print(acc)