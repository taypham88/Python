'''execution code for problem 1 of year 2023 advent of code'''
# Advent of Code
#--- Day 1: Trebuchet?! ---

import os

current_directory = os.getcwd()
file_name = 'input_file.txt'
file_path = os.path.join(current_directory, file_name)
ans1, ans2 = 0, 0
checker = ['one', 'two','three','four', 'five', 'six', 'seven', 'eight', 'nine']

with open(file_path, 'r') as file:

    for line in file:
        part1 = []
        part2 = []
        for i, c in enumerate(line):
            if c.isdigit():
                part1.append(c)
                part2.append(c)
            for d, val in enumerate(checker):
                if line[i:].startswith(val):
                    part2.append(str(d+1))
        ans1 += int(part1[0] + part1[-1])
        ans2 += int(part2[0] + part2[-1])

print(ans1)
print(ans2)