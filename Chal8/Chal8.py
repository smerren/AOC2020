instArray = []
counter = 0
acc = 0
counterArray = []

with open("input8.txt", "r") as file:
    for line in file:
        line = line.strip()
        lineTemp = line.split(" ")
        instArray.append(lineTemp)

while True:
    if instArray[counter][0] == "nop":
        counter += 1

    elif instArray[counter][0] == "acc":
        acc += int(instArray[counter][1])
        counter += 1

    elif instArray[counter][0] == "jmp":
        counter += int(instArray[counter][1])

    if counter in counterArray:
        break
    else:
        counterArray.append(counter)

print(acc)
