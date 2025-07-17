total = 0


def validater(input):
    test = input[4:-1]
    number_len = 0
    comma_seen = False

    left = ""
    right = ""
    t = ""
    if input[-1] != ')':
        return False, 0, 0
    for letter in test:
        try:
            letter = int(letter)
        except:
            a = 1
        if number_len > 3:
            return False, 0, 0
        elif isinstance(letter, int):
            number_len += 1
            t += str(letter)
        elif letter == ',' and not comma_seen:
            left = t
            t = ''
            comma_seen = True
            number_len = 0
        else:
            return False, 0, 0
    right = t
    return True, left, right


with open("input.txt") as f:
    temp = ""
    temp2 = ""
    do = True

    string = "don't()"
    for x in f:
        i = 0
        possible = False
        for c in x:
            temp += str(x[i:i + 4])
            temp2 += str(x[i:i + 7])

            if temp == "do()":
                print("We are currently in a state of DO")
                do = True
            try:
                if temp2[4] == "'":
                    temp3 = ""
                    temp3 += temp2[1:4] + temp2[5:]
                    if temp3 == "dont()":
                        print("We are currently in a state of DON'T")
                        do = False
            except:
                a = 1

            j = i + 4
            if temp == "mul(" and do:
                while j < i + 12:
                    if x[j] == ')':
                        temp += x[j]
                        break
                    else:
                        temp += x[j]
                        j += 1

                result = validater(temp)
                if result[0]:
                    print("Found a valid result. Total string: {}. Left input: {}, right input: {}".format(temp,
                                                                                                           result[1],
                                                                                                           result[2]))
                    total += int(result[1]) * int(result[2])
            temp = ""
            temp2 = " "
            i += 1

    print("The total result is: " + str(total))
