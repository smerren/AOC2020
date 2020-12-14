busID = []

def inv(a, m):
    m0 = m
    x0 = 0
    x1 = 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        t = m
        m = a % m
        a = t
        t = x0
        x0 = x1 - q * x0
        x1 = t
    if x1 < 0:
        x1 = x1 + m0
    return x1

def findMinX(num, rem, k):
    prod = 1
    for i in range(0, k):
        prod = prod * num[i]
    result = 0

    for i in range(0, k):
        pp = prod // num[i]
        result = result + rem[i] * inv(pp, num[i]) * pp

    return result % prod

counter = 0
with open("test.txt", "r") as file:
    for line in file:
        line = line.strip()
        if len(line) < 8:
            earliest = int(line)
        else:
            line = line.split(",")
            for i in line:
                if i != 'x':
                    busID.append([int(i), counter])
                counter += 1

num = [busID[i][0] for i in range(len(busID))]
rem = [(busID[i][0]-busID[i][1])%busID[i][0] for i in range(len(busID))]
print(findMinX(num, rem, len(busID)))


# x mod mi = ri mod mi
# x mod busID[i] = num[i] mod busID[i]
#x mod busID[i] = mods[i]