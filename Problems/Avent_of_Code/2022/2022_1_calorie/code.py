#--- Advent of code 2022 ---
#--- Day 1: Calorie Counting ---
temp = []

with open('2022_1_calorie/input_file.txt') as file:
    [temp.append(line.rstrip()) for line in file]

total, ans = 0, []
for i in temp:
    if i != '':
        total += int(i)
    else:
        ans.append(total)
        total = 0
# Part 2
ans2 = 0
ans.sort()
for i in range(3):
    ans2 += ans.pop(-1)
print(ans2)