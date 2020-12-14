# 0 = E, 1 = S, 2 = W, 3 = N
#x and y
# +Y = N, -Y = S, +X = E, -X = W
waypoint = [10, 1]
ship = [0, 0]

with open("input12.txt", "r") as file:
    for line in file:
        line = line.strip()
        line = [line[0], int(line[1:])]
        print(ship, waypoint)
        if line[0] == "F":
            ship[0] += waypoint[0]*line[1]
            ship[1] += waypoint[1]*line[1]

        elif line[0] == "R":
            if line[1] == 90:
                waypoint = [waypoint[1], -waypoint[0]]
            elif line[1] == 180:
                waypoint = [-waypoint[0], -waypoint[1]]
            elif line[1] == 270:
                waypoint = [-waypoint[1], waypoint[0]]

        elif line[0] == "L":
            if line[1] == 90:
                waypoint = [-waypoint[1], waypoint[0]]
            elif line[1] == 180:
                waypoint = [-waypoint[0], -waypoint[1]]
            elif line[1] == 270:
                waypoint = [waypoint[1], -waypoint[0]]

        elif line[0] == "N":
            waypoint[1] += line[1]

        elif line[0] == "E":
            waypoint[0] += line[1]

        elif line[0] == "S":
            waypoint[1] -= line[1]

        elif line[0] == "W":
            waypoint[0] -= line[1]

for i in range(len(ship)):
    if ship[i] < 0:
        ship[i] = abs(ship[i])

print(sum(ship))
