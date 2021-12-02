dataset = open("input1.txt").read().splitlines()
dataset = [int(entry) for entry in dataset] # convert all to int
def pog():
    for a in dataset:
        for b in dataset:
            if a + b == 2020:
                return a*b
print(pog())

