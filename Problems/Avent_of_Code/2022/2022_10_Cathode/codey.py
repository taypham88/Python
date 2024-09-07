#--- Advent of code 2022 ---
#--- Day 10: Cathode-Ray Tube ---

programs = []
with open('2022_10_Cathode/input_file.txt') as file:
    for line in file:
        line = line.rstrip().split(' ')
        if line[0] == 'noop':
            programs.append([line[0], 0])
        else:
            programs.append([line[0], int(line[1])])


cycle = 0
x = 1
tracking = []

for i in programs:
    if i[0] == 'noop':
        cycle += 1
        tracking.append([cycle,x])
    if i[0] == 'addx':
        cycle += 1
        tracking.append([cycle,x])
        cycle += 1
        tracking.append([cycle,x])
        x += i[1]

# print(tracking[19],tracking[59],tracking[99],tracking[139],tracking[179],tracking[219])
# ans = [tracking[19],tracking[59],tracking[99],tracking[139],tracking[179],tracking[219]]
# res = 0
# for i in ans:
#     res += i[0]*i[1]
# print(res)
# Part 2 print screen

def drawPoint(cycle,x):
    sprite = [x,x+1,x+2]
    if cycle in sprite:
        return '#'
    else:
        return '.'

line = ''

for i in tracking:
    location = i[0] % 40
    # print(i, location)
    line += drawPoint(location,i[1])
    if len(line) == 40:
        print(line)
        line = ''







