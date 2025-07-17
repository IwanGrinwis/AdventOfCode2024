rules = []
total = 0
total2 = 0
faulty = []


def create_rules():
    with open("rules.txt") as f:
        for x in f:
            left = ""
            right = ""
            second = False
            for c in x:
                if c == "\n":
                    break
                elif c == "|":
                    second = True
                elif second:
                    right += c
                elif not second:
                    left += c

            rules.append((left, right))


def validater(numbers):
    seen = []
    for num in numbers:
        i = 0
        while i < len(rules):
            if rules[i][1] == num and rules[i][0] not in seen and rules[i][0] in numbers:
                return False
            i += 1
        seen.append(num)
    return True

def validater2(cheese):
    new_list = cheese.copy()
    counter = 0
    seen = []
    for num in cheese:
        i = 0
        while i < len(rules):
            if rules[i][1] == num and rules[i][0] not in seen and rules[i][0] in cheese:
                pos = cheese.index(rules[i][0])
                new_list[counter], new_list[pos] = new_list[pos], new_list[counter]
            i += 1
        counter += 1

        seen.append(num)

    return new_list


create_rules()
with open("input.txt") as f:
    for x in f:
        numbers = []
        valid = True
        temp = ""

        for c in x:
            if c == ",":
                numbers.append(temp)
                temp = ""
            elif c == "\n":
                a = 0
            else:
                temp += c
        numbers.append(temp)
        valid = validater(numbers)

        if valid:
            total += int(numbers[int(len(numbers) / 2)])
        else:
            faulty.append(numbers)

print("Starting on part 2")

for l in faulty:
    new_list = validater2(l)

    while new_list != validater2(new_list):
        new_list = validater2(new_list)

    if validater(new_list):
        total2 += int(new_list[int(len(new_list) / 2)])
    else:
        print("Not valid!")

print(total)
print(total2)
