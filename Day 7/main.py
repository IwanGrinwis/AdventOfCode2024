results = []
numbers = []
total = 0
total2 = 0

def testInput(num_list, exp, index, concat, result):
    if index >= len(num_list):
        return result

    next = num_list[index]
    plus = testInput(num_list, exp, index + 1, concat, result + next)
    mul = testInput(num_list, exp, index + 1, concat, result * next)
    conc = -1

    if concat:
        conc = testInput(num_list, exp, index + 1, True, int((str(result)+"" + str(next))))
    if plus == int(exp) or mul == int(exp) or conc == int(exp):
        return int(exp)
    else:
        return -1


with open("input.txt") as f:
    for x in f:
        temp1, temp2 = x.split(":")
        results.append(temp1)

        templist = []
        temp3 = ""
        for c in temp2:
            if c.isnumeric():
                temp3 += c
            elif temp3 != "":
                templist.append(int(temp3))
                temp3 = ""
            else:
                a = 1
        if temp3 != "":
            templist.append(int(temp3))
        numbers.append(templist)

counter = 0
for l in numbers:
    test = testInput(l, results[counter], 1, False, l[0])

    if int(test) == int(results[counter]):
        total += test
    counter += 1
print(total)

counter = 0
for l in numbers:
    test = testInput(l, results[counter], 1, True, l[0])

    if int(test) == int(results[counter]):
        total2 += test
    counter += 1
print(total2)
