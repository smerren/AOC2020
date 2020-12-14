import re

fields = ["byr:", "iyr:", "eyr:", "hgt:", "hcl:", "ecl:", "pid:"]
counter = 0
validPassports = 0
with open("cred.txt", "r") as file:
    for line in file:
        line = line.strip().split(" ")
        for i in fields:
            for j in line:
                if i in j:
                    validation = j.split(":")[1]
                    if i == "byr:" and 1920 <= int(validation) <= 2002:
                        counter += 1
                    elif i == "iyr:" and 2010 <= int(validation) <= 2020:
                        counter += 1
                    elif i == "eyr:" and 2020 <= int(validation) <= 2030:
                        counter += 1
                    elif i == "hgt:" and re.match('(1([5-8][0-9]|9[0-3])cm)|((59|6[0-9]|7[0-6])in)', validation):
                        counter += 1
                    elif i == "hcl:" and re.match('#(([0-9]|[a-f]){6})', validation):
                        counter += 1
                    elif i == "ecl:" and re.match('(amb|blu|brn|gry|grn|hzl|oth)', validation):
                        counter += 1
                    elif i == "pid:" and re.match('[0-9]{9}', validation):
                        counter += 1

        if line[0] == "":
            if counter == len(fields):
                validPassports += 1
            counter = 0

print(validPassports)

