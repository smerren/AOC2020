# 0 = E, 1 = S, 2 = W, 3 = N
face = [[1, 0], [0, -1], [-1, 0], [0, 1]]
angleChange = 0
#x and y
# +Y = N, -Y = S, +X = E, -X = W
direction = [0, 0]

with open("input12.txt", "r") as file:
    for line in file:
        line = line.strip()
        line = [line[0], int(line[1:])]
        print(direction)
        if line[0] == "F":
            for i in range(len(face[angleChange])):
                if face[angleChange][i] > 0:
                    direction[i] += line[1]
                elif face[angleChange][i] < 0:
                    direction[i] -= line[1]

        elif line[0] == "R":
            angleChange += (line[1]/360)*4
            angleChange = int(angleChange%4)
            print(angleChange)

        elif line[0] == "L":
            angleChange -= (line[1]/360)*4
            angleChange = int(angleChange%4)
            print(angleChange)

        elif line[0] == "N":
            direction[1] += line[1]

        elif line[0] == "E":
            direction[0] += line[1]

        elif line[0] == "S":
            direction[1] -= line[1]

        elif line[0] == "W":
            direction[0] -= line[1]

print(direction)

for i in range(len(direction)):
    if direction[i] < 0:
        direction[i] = abs(direction[i])

print(sum(direction))
