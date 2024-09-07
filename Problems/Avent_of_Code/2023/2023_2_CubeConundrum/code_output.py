'''execution code for problem 2 of year 2023 advent of code'''
# Advent of Code
#--- Day 2: Cube Conundrum ---

import os

current_directory = os.getcwd()
file_name = 'input_file.txt'
file_path = os.path.join(current_directory, file_name)
compareHash = {'red': 12, 'blue' : 14, 'green': 13}
part1, part2 = 0, 0

with open(file_path, 'r') as file:

    for idx, line in enumerate(file):
        temp = line[7:].strip().replace(',','').split(';')
        GAMEFAIL = False
        # for part 2. keeps track of the max of each color
        maxHash = {'red': 0, 'blue' : 0, 'green': 0}
        for game in temp:
            item = game.strip().split(' ')
            countHash = {'red': 0, 'blue' : 0, 'green': 0}
            for i,obj in enumerate(item):
                if obj in compareHash:
                    maxHash[obj] = max(maxHash[obj], int(item[i-1]))
                    if not GAMEFAIL:
                        countHash[obj] += int(item[i-1])
            for k,v in compareHash.items():
                if v < countHash[k] and not GAMEFAIL:
                    GAMEFAIL = True
                    break
        if not GAMEFAIL:
            part1 += idx + 1
        # Part 2, applies product of the max of each color to answer per problem conditions
        part2 += maxHash['red'] * maxHash['blue'] * maxHash['green']

print(part1)
print(part2)