from itertools import product
mem = {}
mask = 0
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
            address = bin(int(address)).replace("0b", "")
            address = list(str(address).zfill(len(mask)))

            for i in range(len(mask)):
                if mask[i] != '0':
                    address[i] = mask[i]

            counter=0
            combinations = []

            for i in address:
                if i == "X":
                    counter+=1

            lst = list(product(range(2), repeat=counter))
            lst = [('{}' * len(t)).format(*t).strip() for t in lst]
            lst = list(map(list, lst))

            for i in range(len(lst)):
                counter = 0
                newAddress = ""
                for j in range(len(address)):
                    if address[j] == "X":
                        newAddress += lst[i][counter]
                        counter+=1
                    else:
                        newAddress += address[j]
                combinations.append(newAddress)

            result = [int(i, 2) for i in combinations]
            for i in result:
                mem[i] = value

    sum = 0
    for i in mem.values():
        sum += int(i)
    print(sum)