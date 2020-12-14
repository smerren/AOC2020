counter = 0

with open("input2.txt", "r") as file:
    for line in file:
        numberRange = (int(line.split("-")[0]), int(line.split("-")[1].split(" ")[0]))
        letterToFind = line.split(" ")[1].strip(":")
        password = line.split(" ")[-1].strip()
        if letterToFind == password[numberRange[0]-1] and letterToFind != password[numberRange[1]-1]:
            counter += 1
        if letterToFind != password[numberRange[0]-1] and letterToFind == password[numberRange[1]-1]:
            counter += 1

print(counter)