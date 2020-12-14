counter = 0
lst = []

with open("input9.txt", "r") as file:
    for line in file:
        line = line.strip()
        if counter == 25:
            break
        else:
            lst.append(line)
            counter += 1

with open("input9.txt", "r") as file:
    counter = 0
    lineCounter = 0
    for line in file:
        line = line.strip()
        found = False
        if lineCounter >= 25:
            for i in lst:
                for j in lst:
                    if int(i) + int(j) == int(line):
                        lst = lst[1:] + [line]
                        found = True
                    if found:
                        break
                if found:
                    break

            if not found:
                print(line)
                break

        lineCounter += 1
