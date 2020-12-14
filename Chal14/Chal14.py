mem = {}

mask = 000000000000000000000000000000000000
address = 0
value = 0

with open("input14.txt", "r") as file:
    for line in file:
        line = line.strip()
        if "mask" in line:
            mask = line.split(" = ")[1]
        else:
            address = line.split(" = ")[0][4:-1]
            value = line.split(" = ")[1]
            value = bin(int(value)).replace("0b", "")
            value = list(str(value).zfill(len(mask)))

            for i in range(len(mask)):
                if mask[i] == "X":
                    continue
                else:
                    value[i] = mask[i]

            mem[address] = "".join(value)

    sum = 0
    for i in mem.values():
        sum += int(i, 2)

    print(sum)