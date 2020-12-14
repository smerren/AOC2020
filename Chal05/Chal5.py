import os, itertools

listOfRows = []
tempListOfRows = []
listOfColumns = [0, 1, 2, 3, 4, 5, 6, 7]
tempListOfColumns = [0, 1, 2, 3, 4, 5, 6, 7]

seatsList = []

for i in range(0, 128):
    listOfRows.append(i)
    tempListOfRows.append(i)

with open("input5.txt", "r") as file:
    for line in file:
        for i in line:
            if i == "F":
                tempListOfRows = tempListOfRows[:len(tempListOfRows)//2]
            if i == "B":
                tempListOfRows = tempListOfRows[len(tempListOfRows)//2:]
            if i == "R":
                tempListOfColumns = tempListOfColumns[len(tempListOfColumns) // 2:]
            if i == "L":
                tempListOfColumns = tempListOfColumns[:len(tempListOfColumns) // 2]

        seatID = (int(tempListOfRows[0])*8) + int(tempListOfColumns[0])
        seatsList.append(str(tempListOfRows[0]) + " " + str(tempListOfColumns[0]))

        tempListOfColumns = listOfColumns
        tempListOfRows = listOfRows

seatsList.sort()
groupedSeatsList = [list(g) for _, g in itertools.groupby(seatsList, lambda x: x.split(" ")[0])]
for i in groupedSeatsList:
    if len(i) < 8:
        print(i)