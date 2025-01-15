#--- Advent of code 2024---
#--- Day 4: Ceres Search ---
import os


current_directory = os.getcwd()
file_name = 'input.txt'
file_path = os.path.join(current_directory, file_name)

INPUT = []
with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
        INPUT.append(line.strip())

row, col = len(INPUT), len(INPUT[0])
'''This was for part 1'''
# def check_word(x,y,direction):
#     dx, dy = direction
#     WORD = 'XMAS'

#     for i in range(1,len(WORD)):

#         if (x+dx < 0 or x+dx >= row) or (y+dy < 0 or y+dy >= col):
#             return False
#         if INPUT[x+dx][y+dy] != WORD[i]:
#             return False
#         x += dx
#         y += dy

#     return True

# def lookup(x,y):
#     direction = ((-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1))
#     TOTAL = 0
#     for dx,dy in direction:
#         if check_word(x,y, (dx,dy)):
#             TOTAL += 1
#     return TOTAL

# Part 2 Change to MAS/MAS Puzzle
'''part 2 lookup function'''

def lookup(x,y):
    POINTS = [(x-1,y-1), (x-1,y+1), (x+1,y-1), (x+1,y+1)]

    for (x,y) in POINTS:
        if x < 0 or x >= row or y < 0 or y >= col:
            return 0

    LOOKUP = [INPUT[x][y] for (x,y) in POINTS]

    # Check (LOOKUP[0], LOOKUP[3]) is either ('M','S') or ('S','M')
    if (LOOKUP[0], LOOKUP[3]) not in [('M','S'), ('S','M')]:
        return 0

    # Check (LOOKUP[1], LOOKUP[2]) is either ('M','S') or ('S','M')
    if (LOOKUP[1], LOOKUP[2]) not in [('M','S'), ('S','M')]:
        return 0

    return 1

COUNT = 0
for i in range(row):
    for j in range(col):
        if INPUT[i][j] == 'A': # Change to A for part 2
            COUNT += lookup(i,j)

print(COUNT)