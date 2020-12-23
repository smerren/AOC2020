ll = [int(x) for x in open('input23.txt').read().strip()]
maxTurns = 10000000
dic = {}
cup = ll[0]

for i in range(1, len(ll)+1):
    if i == len(ll):
        dic[ll[i - 1]] = 10
        break
    else:
        dic[ll[i-1]] = ll[i]

for i in range(10, 1000001):
    if i == 1000000:
        dic[i] = ll[0]
    else:
        dic[i] = i+1

for _ in range(maxTurns+1):
    next = dic[cup]
    picked = []
    for i in range(3):
        picked.append(next)
        next = dic[next]
    dic[cup] = next
    cupMinusOne = cup - 1
    if cupMinusOne == 0:
        cupMinusOne = 1000000
    while cupMinusOne in picked:
        if cup > 1:
            cupMinusOne -= 1
        if cupMinusOne == 0:
            cupMinusOne = 1000000

    l = dic[cupMinusOne]
    dic[cupMinusOne] = picked[0]
    dic[picked[2]] = l
    cup = next

print(dic[1] * dic[dic[1]])