with open("input1.txt", "r") as file:
    for line in file:
        strippedLine = line.strip()
        with open("input1.txt", "r") as anotherFile:
            for anotherLine in anotherFile:
                anotherStrippedLine = anotherLine.strip()
                with open("input1.txt", "r") as finalFile:
                    for finalLine in finalFile:
                        finalStrippedLine = finalLine.strip()

                        if strippedLine == anotherStrippedLine == finalLine:
                            continue
                        else:
                            if int(strippedLine) + int(anotherStrippedLine) + int(finalStrippedLine) == 2020:
                                print(line, anotherLine, finalStrippedLine)