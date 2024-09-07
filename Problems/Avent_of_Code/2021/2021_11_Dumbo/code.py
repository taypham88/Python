# Advent of Code
#--- Day 11: Dumbo Octopus ---

octopuses = []
flashes = 0
with open('2021_11_Dumbo/input_file.txt') as file:

    for line in file:
        positions = []
        temp = list(line.rstrip())
        for i in temp:
            positions.append(int(i))
        octopuses.append(positions)

def flash(level, pos):

    if level -1 > -1: # top
        octopuses[level-1][pos] += 1
        if octopuses[level-1][pos] > 9 and [level-1, pos] not in flashed and [level-1, pos] not in flashing:
            flashing.append([level-1, pos])

    if level - 1 > -1 and pos - 1 > -1: # top left
        octopuses[level-1][pos-1] += 1
        if octopuses[level-1][pos-1] > 9 and [level-1, pos-1] not in flashed and [level-1, pos-1] not in flashing:
            flashing.append([level-1, pos-1])

    if level - 1 > -1 and pos + 1 < len(octopuses[level]): # top right
        octopuses[level-1][pos+1] += 1
        if octopuses[level-1][pos+1] > 9 and [level - 1, pos + 1] not in flashed and [level - 1, pos + 1] not in flashing:
            flashing.append([level - 1, pos + 1])

    if pos - 1 > -1: # left
        octopuses[level][pos-1] += 1
        if octopuses[level][pos-1] > 9 and [level, pos-1] not in flashed and [level, pos-1] not in flashing:
            flashing.append([level, pos-1])

    if pos + 1 < len(octopuses[level]): # right
        octopuses[level][pos+1] += 1
        if octopuses[level][pos+1] > 9 and [level, pos+1] not in flashed and [level, pos+1] not in flashing:
            flashing.append([level, pos+1])

    if level + 1 < len(octopuses): # bottom
        octopuses[level+1][pos] += 1
        if octopuses[level+1][pos] > 9 and [level+1, pos] not in flashed and [level+1, pos] not in flashing:
            flashing.append([level+1, pos])

    if level + 1 < len(octopuses) and pos - 1 > -1: # bottom left
        octopuses[level+1][pos-1] += 1
        if octopuses[level+1][pos-1] > 9 and [level+1, pos-1] not in flashed and [level+1, pos-1] not in flashing:
            flashing.append([level+1, pos-1])

    if level + 1 < len(octopuses) and pos + 1 < len(octopuses[level]): # bottom right
        octopuses[level+1][pos+1] += 1
        if octopuses[level+1][pos+1] > 9 and [level+1, pos+1] not in flashed and [level+1, pos+1] not in flashing:
            flashing.append([level+1, pos+1])
    return

# part two compare the size of flashed to size of input matrix, which is 100
for count in range(225):
    flashing = []
    flashed = []


    for level in range(len(octopuses)):
        for pos in range(len(octopuses[level])):
            octopuses[level][pos] += 1
            if octopuses[level][pos] > 9:
                flashing.append([level,pos])


    while len(flashing) > 0:
        level, pos = flashing.pop()
        flashed.append([level, pos])
        flash(level, pos)

    for level in range(len(octopuses)):
        for pos in range(len(octopuses[level])):
            if octopuses[level][pos] > 9:
                octopuses[level][pos] = 0

    if len(flashed) == 100:
        print('answer is', count + 1)

    flashes += len(flashed)

print(flashes)
for i in octopuses:
    print(i)
