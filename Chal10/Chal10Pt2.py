adapters = [0]
adapterTree = []
sum = []
size = []
counter = 0

with open("input10.txt") as file:
    for line in file:
        line = line.strip()
        adapters.append(int(line))

adapters = sorted(adapters)
adapters.append(adapters[-1]+3)
start = adapters[0]

while True:
    adapterTree.append(start)

    if start+1 in adapters:
        start += 1

    elif start+3 in adapters:
        start += 3

    elif start in adapterTree:
        break

sum = [j-i for i, j in zip(adapterTree[:-1], adapterTree[1:])]
for i in sum:
    if i == 1:
        counter += 1
    if i == 3:
        if counter >= 2:
            size.append(counter)
        counter = 0

result = 1
for i in size:
    if i == 4:
        result = result * 7
    if i == 3:
        result = result * 4
    if i == 2:
        result = result * 2

print(result)