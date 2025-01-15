#--- Advent of code 2024---
#--- Day 3: Mull It Over ---
import os
import re

current_directory = os.getcwd()
file_name = 'input.txt'
file_path = os.path.join(current_directory, file_name)

total = 0
pattern = r"mul\((\d+),\s*(\d+)\)|do\(\)|don't\(\)"  # Regex to match mul(x, y)
start = True

with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
        # Use finditer for better control over matches
        for match in re.finditer(pattern, line):
            if match.group() == "don't()":
                start = False
            elif match.group() == 'do()':
                start = True
            elif start:
                x, y = int(match.group(1)), int(match.group(2)) # Convert to integers
                total += x * y  # Multiply and add to total
print(total)

