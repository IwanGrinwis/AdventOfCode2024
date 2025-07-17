safe = 0
safe2 = 0


def safe_checker(nums):
    counter = 0
    inc = False

    if nums[0] < nums[1]:
        inc = True
    if nums[0] == nums[1]:
        return False

    for n in nums:
        if inc:
            try:
                if n >= nums[counter + 1] or abs(n - nums[counter + 1]) > 3 or abs(n - nums[counter + 1]) == 0:
                    return False
            except:
                a = 1

        else:
            try:
                if n <= nums[counter + 1] or abs(n - nums[counter + 1]) > 3 or abs(n - nums[counter + 1]) == 0:
                    return False
            except:
                a = 1

        counter += 1

    return True


def safe_checker_2(nums):
    if safe_checker(nums):
        return True

    c = 0
    for n in nums:
        templist = nums.copy()
        templist.pop(c)
        if safe_checker(templist):
            return True
        c += 1

    return False


with open("input.txt") as f:
    for x in f:
        temp = ""
        numbers = []
        for c in x:
            if c.isnumeric():
                temp += c
            elif c == " ":
                numbers.append(int(temp))
                temp = ""
        numbers.append(int(temp))

        if safe_checker(numbers):
            safe += 1

        if safe_checker_2(numbers):
            safe2 += 1

print("Question 1 answer: {}".format(safe))
print("Question 2 answer: {}".format(safe2))

