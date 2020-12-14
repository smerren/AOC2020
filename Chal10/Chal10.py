adapters = []
adapterTree = []
sum = []

with open("input10.txt") as file:
    for line in file:
        line = line.strip()
        adapters.append(int(line))

adapters = sorted(adapters)

start = adapters[0]
while True:
    adapterTree.append(start)

    if start+1 in adapters:
        start += 1

    elif start+3 in adapters:
        start += 3

    elif start in adapterTree:
        break

sum = [j-i for i, j in zip(adapterTree[:-1], adapterTree[1:])] + [adapterTree[0]] + [3]
print(sum.count(3) * sum.count(1))


