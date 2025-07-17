rows = []
visited = []
with open("input.txt") as f:  # Add all input rows to a list of lists
    for x in f:
        x = x.rstrip("\n")
        rows.append(x)

pos = (0, 0)

j = 0
done = False
for row in rows:  # Get starting position
    i = 0
    for p in row:
        if p == "^":
            pos = (i, j)
            done = True
            break
        i += 1
    if done:
        break
    j += 1

facing = 0
new_pos = (0, 0)


def check_pos(position, face):
    if rows[position[1]][position[0]] == "#":
        face += 1
        face = face % 4
    else:
        visited.append(position)
    return face


while 0 < pos[0] < 130 and 0 < pos[1] < 130:
    if facing == 0:  # Facing up
        new_pos = (pos[0], pos[1] - 1)

    elif facing == 1:  # Facing right
        new_pos = (pos[0] + 1, pos[1])

    elif facing == 2:  # Facing down
        new_pos = (pos[0], pos[1] + 1)

    elif facing == 3:  # Facing left
        new_pos = (pos[0] - 1, pos[1])

    new_facing = check_pos(new_pos, facing)

    if facing == new_facing:
        pos = new_pos
    else:
        facing = new_facing

question1 = list(dict.fromkeys(visited))
print("Total steps for question 1: " + str(len(question1) + 1))
