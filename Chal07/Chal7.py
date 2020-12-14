dictionary = {}
listOfBagsThatLeadToGold = []

def _finditeminlist(list, key):
    if key in list:
        return True
    for item in list:
        newItem = _finditeminlist(dictionary[item], key)
        if newItem is not None:
            return newItem

def _finditem(obj, key):
    for k,v in obj.items():
        item = _finditeminlist(v, key)
        if item is not None:
            listOfBagsThatLeadToGold.append(k)
            continue

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
        lst = [e[3:] if "bags" not in e else e[3:-1] for e in contents]
        dictionary[bag] = lst

_finditem(dictionary, 'shiny gold bag')
print(len(listOfBagsThatLeadToGold))
