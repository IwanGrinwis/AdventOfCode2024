l = []  # Left list
r = []  # Right list
total = 0


def q1():  # Question 1
    count = 0
    t = 0
    for n in l:
        t += abs(n - r[count])
        count += 1
    return t


def q2():  # Question 2
    result = 0
    for i in l:
        a = 0
        for j in r:
            if i == j:
                a += 1
            elif i < j:
                break

        result += i * a
    return result


with open("input.txt") as f:
    for x in f:  # For reach line in file f (input.txt)
        counter = 0
        left = ""
        right = ""
        for c in x:  # for characters in line x
            if counter < 5:
                left += c

            if counter > 5:
                right += c

            counter += 1
        l.append(int(left))
        r.append(int(right))
    l.sort()
    r.sort()

    print("Answer to part 1: {}".format(q1()))
    print("Answer to part 2: {}".format(q2()))
