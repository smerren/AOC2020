input = [int(line) for line in open('input15.txt').read().strip().split(",")]
turnNumber = len(input)
lastTime = len(input)
lastSpoken = {}
newNumber = 0
for i, v in enumerate(input):
    lastSpoken[v] = i+1

while turnNumber <= 30000000:
    if lastTime == turnNumber-1:
        lastTime = lastSpoken[0]
        lastSpoken[0] = turnNumber
    else:
        newNumber = (turnNumber-1) - lastTime
        if newNumber in lastSpoken:
            lastTime = lastSpoken[newNumber]
        else:
            lastTime = turnNumber
        lastSpoken[newNumber] = turnNumber
    turnNumber += 1

print(newNumber)