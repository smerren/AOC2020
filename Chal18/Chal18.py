def recurse(lst, i):
    result = 0
    while i < len(lst):
        if i == 0 and lst[i] != ')' and lst[i] != '(':
            result = int(lst[i])
            i += 1
        elif lst[i] == '(':
            recur = recurse(lst, i+1)
            result += recur[0]
            i += recur[1] - i+1
        elif lst[i] == "+" and lst[i+1] != '(':
            result += int(lst[i+1])
            i += 2
        elif lst[i] == "*" and lst[i+1] != '(':
            result *= int(lst[i+1])
            i += 2
        elif lst[i] == "+" and lst[i+1] == '(':
            recur = recurse(lst, i+2)
            result += recur[0]
            i += recur[1] - i+1
        elif lst[i] == "*" and lst[i+1] == "(":
            recur = recurse(lst, i+2)
            result *= recur[0]
            i += recur[1] - i+1
        elif lst[i] == ")":
            return result, i
        else:
            result += int(lst[i])
            i+=1


    return result, i

s = 0
with open("input18.txt", "r") as file:
    for line in file:
        op = []
        line = line.strip()
        line = line.replace(" ", "")
        for i in line:
                op.append(i)
        s += recurse(op, 0)[0]

print(s)

