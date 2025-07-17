total = 0
input = []

def question1():
    j = 0
    total = 0
    for row in input:
        i = 0
        for letter in row:

            if letter == "X":
                try:
                    temp = row[i - 3:i + 1]
                    if temp == "SAMX":
                        total += 1
                except:
                    a = 0
                try:
                    temp2 = row[i:i + 4]
                    if temp2 == "XMAS":
                        total += 1
                except:
                    a = 0
                try:
                    if j > 2 and i > 2:
                        temp3 = letter + input[j - 1][i - 1] + input[j - 2][i - 2] + input[j - 3][i - 3]
                        if temp3 == "XMAS":
                            total += 1

                except:
                    a = 0
                try:
                    if j < 137 and i < 137:
                        temp4 = letter + input[j + 1][i + 1] + input[j + 2][i + 2] + input[j + 3][i + 3]
                        if temp4 == "XMAS":
                            total += 1
                except:
                    a = 0

                try:
                    if j > 2 and i < 137:
                        temp5 = letter + input[j - 1][i + 1] + input[j - 2][i + 2] + input[j - 3][i + 3]
                        if temp5 == "XMAS":
                            total += 1
                except:
                    a = 0
                try:
                    if j < 137 and i > 2:
                        temp6 = letter + input[j + 1][i - 1] + input[j + 2][i - 2] + input[j + 3][i - 3]
                        if temp6 == "XMAS":
                            total += 1
                except:
                    a = 0

                try:
                    if j > 2:
                        temp7 = letter + input[j - 1][i] + input[j - 2][i] + input[j - 3][i]
                        if temp7 == "XMAS":
                            total += 1
                except:
                    a = 0

                try:
                    if j < 137:
                        temp8 = letter + input[j + 1][i] + input[j + 2][i] + input[j + 3][i]
                        if temp8 == "XMAS":
                            total += 1
                except:
                    a = 0
            i += 1
        j += 1
    return total

def question2():
    j = 0
    total = 0
    for row in input:
        i = 0
        for letter in row:
            if letter == "A":
                if 0 < j < 139 and 0 < i < 139:
                    temp1 = input[j-1][i-1] + letter + input[j+1][i+1]
                    temp2 = input[j-1][i+1] + letter + input[j+1][i-1]

                    if temp1 == "MAS" or temp1 == "SAM":
                        if temp2 == "MAS" or temp2 == "SAM":
                            total += 1
            i += 1
        j += 1
    return total




with open("input.txt") as f:
    for x in f:
        input.append(x)

total = question1()
total2 = question2()
print("Question 1: " + str(total))
print("Question 2: " + str(total2))