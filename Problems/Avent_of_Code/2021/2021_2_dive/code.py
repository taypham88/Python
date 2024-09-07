# Advent of Code
#--- Day 2: Dive! ---


with open('2021_2_dive/input_file.txt') as file:
    movement = [line.rstrip().split(" ") for line in file]

# part 1
# horizontal = 0
# vertical = 0

# for i in movement:
#     if i[0] == 'forward':
#         horizontal += int(i[1])
#     elif i[0] == 'up':
#         vertical -= int(i[1])
#     else:
#         vertical += int(i[1])

# ans = horizontal * vertical
# print(ans)

# Part 2
horizontal = 0
vertical = 0
aim = 0

for i in movement:
    if i[0] == 'forward':
        horizontal += int(i[1])
        vertical += aim * int(i[1])
    elif i[0] == 'up':

        aim -= int(i[1])
    else:

        aim += int(i[1])

ans = horizontal * vertical
print(ans)