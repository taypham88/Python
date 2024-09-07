#--- Advent of code 2022 ---
#--- Day 2: Rock Paper Scissors ---

# Placement is opponent first then you
score = {'AX': [4,4],
         'AY': [1,8],
         'AZ': [7,3],
         'BX': [8,1],
         'BY': [5,5],
         'BZ': [2,9],
         'CX': [3,7],
         'CY': [9,2],
         'CZ': [6,6]}

input =[]
with open('2022_2_r_p_s/input_file.txt') as file:
    for line in file:
        l,r = line.rstrip().split(' ')
        input.append(l+r)

# Part 1
# opponent = 0
# player = 0
# for item in input:
#     opponent += score[item][0]
#     player += score[item][1]

# print(player)

# Part 2
score2 = {'A': [3,4,8],
         'B': [1,5,9],
         'C': [2,6,7]}

player = 0
for item in input:
    if item[1] == 'X': # Lose
        player += score2[item[0]][0]
    if item[1] == 'Y': # Draw
        player += score2[item[0]][1]
    if item[1] == 'Z': # Win
        player += score2[item[0]][2]

print(player)
