# Advent of Code
#--- Day 10: Syntax Scoring ---

# Input Processing
input =[]
with open('2021_10_Syntax/input_file.txt') as file:
    [input.append(line.rstrip()) for line in file]

compare = {'}':'{', ']':'[', ')':'(', '>':'<'}
score = {')': 3, ']': 57, '}': 1197, '>': 25137}
score2 = {'(': 1, '[': 2, '{': 3, '<': 4}
total, new = 0, []

# Part one just print all scores. modified for part two to discard all corrupted lines.
for line in input:
    temp,total = [],0
    for item in line:
        if item in ('[','{','(', '<'):
            temp.append(item)
        else:
            test = temp.pop()
            if compare[item] != test:
                total += score[item]
    if total == 0:
        new.append(temp)

# Part two
res = []
for line in new:
    ans = 0
    for i in range(len(line)):
        ans = ans*5
        temp = line.pop(-1)
        ans += score2[temp]
    res.append(ans)

res.sort()
print(res[len(res)//2])

