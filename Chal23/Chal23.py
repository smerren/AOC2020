from collections.abc import Iterable

ll = [int(x) for x in open('input23.txt').read().strip()]

def flatten(l):
    for el in l:
        if isinstance(el, Iterable) and not isinstance(el, (str, bytes)):
            yield from flatten(el)
        else:
            yield el

turns = 0
maxTurns = 99
while turns < 100:
    cup = ll[0]
    picked = [ll[1], ll[2], ll[3]]

    cupMinusOne = cup - 1
    newll = [ll[0]] + ll[4:]
    if cupMinusOne == 0:
        cupMinusOne = max(newll)
    if cupMinusOne in picked:
        while cupMinusOne in picked:
            cupMinusOne -= 1
            if cupMinusOne == 0:
                cupMinusOne = max(newll)

    newll.insert(newll.index(cupMinusOne)+1, picked)
    ll = list(flatten(newll))
    if turns == maxTurns:
        ll = ll[ll.index(1)+1:] + ll[:ll.index(1)]
        for i in ll:
            print(i, end="")
        break

    ll = ll[1:] + [ll[0]] # probably have to edit this
    turns += 1

