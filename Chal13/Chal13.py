earliest = 0
buses = []

with open("input13.txt", "r") as file:
    for line in file:
        line = line.strip()
        if len(line) < 8:
            earliest = int(line)
        else:
            line = line.split(",")
            for i in line:
                if i != 'x':
                    buses.append(i)

found = False
for i in range(earliest, (earliest + int(sorted(buses)[-1]))):
    if not found:
        for j in buses:
            if i%int(j) == 0:
                found = True
                print(int(j) * (i - earliest))