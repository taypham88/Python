'''execution code for problem 3 of year 2023 advent of code'''
# Advent of Code
#--- Day 3: Gear Ratios ---

import os
import collections

current_directory = os.getcwd()
file_name = 'input_file.txt'
file_path = os.path.join(current_directory, file_name)
matrix = []

with open(file_path, 'r') as file:

    for idx, line in enumerate(file):
        temp = line.strip()
        matrix.append(temp)

n = len(matrix)
m = len(matrix[0])

def checker(i,j):

    RATIO = False
    GEAR_ID = ''

    # left
    if j > 0 and not matrix[i][j-1].isdigit() and matrix[i][j-1] != '.':
        if matrix[i][j-1] == '*':
            RATIO = True
            GEAR_ID = str(i) + str(j-1)
        return [True, RATIO, GEAR_ID]
    # upper left
    if i > 0 and j > 0 and not matrix[i-1][j-1].isdigit() and matrix[i-1][j-1] != '.':
        if matrix[i-1][j-1] == '*':
            RATIO = True
            GEAR_ID = str(i-1) + str(j-1)
        return [True, RATIO, GEAR_ID]
    # lower left
    if i < n - 1 and j > 0 and not matrix[i+1][j-1].isdigit() and matrix[i+1][j-1] != '.':
        if matrix[i+1][j-1] == '*':
            RATIO = True
            GEAR_ID = str(i+1) + str(j-1)
        return [True, RATIO, GEAR_ID]
    # upper
    if i > 0 and not matrix[i-1][j].isdigit() and matrix[i-1][j] != '.':
        if matrix[i-1][j] == '*':
            RATIO = True
            GEAR_ID = str(i-1) + str(j)
        return [True, RATIO, GEAR_ID]
    # upper right
    if i > 0 and j < m - 1 and not matrix[i-1][j+1].isdigit() and matrix[i-1][j+1] != '.':
        if matrix[i-1][j+1] == '*':
            RATIO = True
            GEAR_ID = str(i-1) + str(j+1)
        return [True, RATIO, GEAR_ID]
    # right
    if j < m - 1 and not matrix[i][j+1].isdigit() and matrix[i][j+1] != '.':
        if matrix[i][j+1] == '*':
            RATIO = True
            GEAR_ID = str(i) + str(j+1)
        return [True, RATIO, GEAR_ID]
    # lower right
    if i < n - 1 and j < m - 1 and not matrix[i+1][j+1].isdigit() and matrix[i+1][j+1] != '.':
        if matrix[i+1][j+1] == '*':
            RATIO = True
            GEAR_ID = str(i+1) + str(j+1)
        return [True, RATIO, GEAR_ID]
    # lower
    if i < n - 1 and not matrix[i+1][j].isdigit() and matrix[i+1][j] != '.':
        if matrix[i+1][j] == '*':
            RATIO = True
            GEAR_ID = str(i+1) + str(j)
        return [True, RATIO, GEAR_ID]

    return [False, RATIO, GEAR_ID]

perv = '.'
NUMB = ''
TOTAL = 0
GEAR = False
ID  =''
TOTALCHECK = []
ALLNUMBS = []
GEARMAP = collections.defaultdict(list)

for i in range(n):
    for j in range(m):

        if matrix[i][j].isdigit() and not perv.isdigit():
            NUMB = matrix[i][j]
            PASS, RATIO, GEAR_ID = checker(i,j)
            if PASS:
                PROCESS = True
            if RATIO:
                GEAR = True
                ID = GEAR_ID
        if matrix[i][j].isdigit() and perv.isdigit():
            NUMB += matrix[i][j]
            PASS, RATIO, GEAR_ID = checker(i,j)
            if PASS:
                PROCESS = True
            if RATIO:
                GEAR = True
                ID = GEAR_ID
        if not matrix[i][j].isdigit() or j == m-1:
            if NUMB != '':
                ALLNUMBS.append(NUMB)
                if PROCESS:
                    TOTALCHECK.append(int(NUMB))
                    TOTAL += int(NUMB)
                    PROCESS = False
                if GEAR:
                    GEARMAP[ID].append(int(NUMB))
                    ID = ''
                    GEAR = False
                NUMB = ''

        perv = matrix[i][j]

PART2 = 0
for k,v in GEARMAP.items():
    if len(v) == 2:
        PART2 += v[0] * v[1]

print(TOTAL) # PART 1
print(PART2)