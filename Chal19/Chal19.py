import lark
def parser(part):
    grammar = r"""start: expr0
    """
    sum = 0
    with open("input19.txt", "r") as file:
        for line in file:
            line = line.strip()
            if part == 2:
                if line[:2] == "8:":
                    line = "8: 42 | 42 8\n"
                if line[:3] == "11:":
                    line = "11: 42 31 | 42 11 31\n"

            if line == "":
                break
            if " 8 " in line or "8:" in line[:2] or " 11 " in line or "11:" in line[:3] or " 0 " in line or "0:" in line[:2]:
                string = "EXPR" + line.replace(" ", " EXPR").replace("EXPR|", "|")
                grammar += string.replace("EXPR11", "expr11").replace("EXPR8", "expr8").replace("EXPR0", "expr0") + "\n"
            elif "a" not in line and "b" not in line:
                grammar += "EXPR" + line.replace(" ", " EXPR").replace("EXPR|", "|") + "\n"
            else:
                grammar += "EXPR" + line + "\n"

        grammar += """
    %import common.LETTER
        """

        p = lark.Lark(grammar, parser='earley',
                           lexer='standard',
                           propagate_positions=False,
                           maybe_placeholders=False)

        for line in file:
            line = line.strip()
            try:
                p.parse(line).pretty()
                sum+=1
            except:
                pass

    print(sum)

# PART 1 AND PART 2, just change integer to either 1 or 2
parser(2)