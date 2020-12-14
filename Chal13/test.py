busses = []

test = {k: int(busses[k]) for k in range(len(busses)) if busses[k] != "x"}

from math import gcd


def lcm(a):  # https://stackoverflow.com/questions/37237954/calculate-the-lcm-of-a-list-of-given-numbers-in-python
    lcmc = a[0]
    for i in a[1:]:
        lcmc = lcmc * i // gcd(lcmc, i)
    return lcmc


def part2():
    i = 0

    def helper(i):
        acceptables = [1]
        for j, num in test.items():
            if not is_divisible(i + j, num):
                return (False, lcm(acceptables))
            else:
                acceptables.append(num)
        return (True, -1)

    while True:
        temp = helper(i)
        if temp[0]:
            return i
        else:
            i += temp[1]


print(part2())