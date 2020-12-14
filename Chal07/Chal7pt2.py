dictionary = {}
numberOfBagsInGold = []

def _findNumberOfBags(obj, key):
    for i in obj[key]:
        bag = [i[:1], i[2:]]
        for i in range(int(bag[0])):
            numberOfBagsInGold.append(bag[1])
            _findNumberOfBags(obj, bag[1])

with open("input7.txt", "r") as file:
    for line in file:
        line = line.strip()
        line = line[:-1]
        line = line.split("contain")
        contents = line[1].split(",")

        for i in contents:
            if "other bag" in i:
                contents.remove(i)

        bag = line[0]
        if bag == "no other bags":
            bag = []
        else:
            bag = bag[:-2]
        lst = [e[1:] if "bags" not in e else e[1:-1] for e in contents]
        dictionary[bag] = lst

_findNumberOfBags(dictionary, 'shiny gold bag')
print(len(numberOfBagsInGold))
