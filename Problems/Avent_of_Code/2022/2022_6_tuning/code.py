#--- Advent of code 2022 ---
#--- Day 6: Tuning Trouble ---

puzzle = ''
with open('2022_6_tuning/input_file.txt') as file:
    for line in file:
        puzzle = line.rstrip()

# Part 1 change sliding window to 4 instead of 14 for part 2
for i in range(0,len(puzzle)-13):
    if len(set(puzzle[i:i+14])) == 14:
        print(i+14)
        break

