#--- Advent of code 2024---
#--- Day 1: Historian Hysteria ---

import os
import collections

current_directory = os.getcwd()
file_name = 'input.txt'
file_path = os.path.join(current_directory, file_name)

first, second = [],[]
with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
        left,right = line.split()
        first.append(int(left))
        second.append(int(right))

first.sort()
second.sort()

TOTAL = 0
# printing total is part 1
for a,b in zip(first,second):
    temp = abs(a-b)
    TOTAL += temp

# Part 2
TOTAL_2 = 0
right_lookup = collections.Counter(second)
for left in first:
    TOTAL_2 += left * right_lookup[left]
print(TOTAL_2)