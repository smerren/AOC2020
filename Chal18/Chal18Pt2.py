# http://www.martinbroadhurst.com/shunting-yard-algorithm-in-python.html
# Having prior knowledge of the Shunting Yard algorithm but having trouble
# implementing it, I decided to grab it off this dude.

import re

def is_number(str):
    try:
        int(str)
        return True
    except ValueError:
        return False

def is_name(str):
    return re.match("\w+", str)

def peek(stack):
    return stack[-1] if stack else None

def apply_operator(operators, values):
    operator = operators.pop()
    right = values.pop()
    left = values.pop()
    values.append(eval("{0}{1}{2}".format(left, operator, right)))

def greater_precedence(op1, op2):
    precedences = {'+': 1, '*': 0}
    return precedences[op1] > precedences[op2]

def evaluate(expression):
    tokens = re.findall("[+/*()-]|\d+", expression)
    values = []
    operators = []
    for token in tokens:
        if is_number(token):
            values.append(int(token))
        elif token == '(':
            operators.append(token)
        elif token == ')':
            top = peek(operators)
            while top is not None and top != '(':
                apply_operator(operators, values)
                top = peek(operators)
            operators.pop()  # Discard the '('
        else:
            # Operator
            top = peek(operators)
            while top is not None and top not in "()" and greater_precedence(top, token):
                apply_operator(operators, values)
                top = peek(operators)
            operators.append(token)
    while peek(operators) is not None:
        apply_operator(operators, values)

    return values[0]

s = 0
with open("input18.txt", 'r') as file:
    for line in file:
        line = line.strip()
        s += evaluate(line)

print(s)
