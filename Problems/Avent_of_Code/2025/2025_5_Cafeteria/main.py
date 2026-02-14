
# Advent of Code
# --- Day 5: Cafeteria ---

import os
from collections import deque
# This gets the directory where main.py is located
script_dir = os.path.dirname(os.path.abspath(__file__))
file_name = 'test.txt'

# This joins the script's folder with the filename
file_path = os.path.join(script_dir, file_name)

with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read().strip()

# Split by the blank line
range_section, id_section = content.split('\n\n')

lookup = []
for line in range_section.splitlines():
    a, b = map(int,line.split('-'))
    lookup.append((a,b))

# Merg Ranges
lookup.sort()
merged = []

start, end = lookup[0]
for nstart, nend in lookup[1:]:

    if nstart <= end + 1:
        end = max(end, nend)

    else:
        merged.append((start, end))
        start, end = nstart, nend

merged.append((start,end))


count = 0
for num1, num2 in merged:
    count += (num2 - num1 + 1)

Total = 0

for l in id_section.splitlines():
    clean_l = l.strip() # Remove whitespace and \n

    current_id = int(clean_l)
    for a, b in lookup:
        if a <= current_id <= b:
            Total += 1
            break

if __name__ == "__main__":
    print(Total)
    print(count)