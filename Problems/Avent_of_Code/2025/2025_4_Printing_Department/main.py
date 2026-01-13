
# Advent of Code
# --- Day 4: Printing Department ---

import os
from collections import deque

# This gets the directory where main.py is located
script_dir = os.path.dirname(os.path.abspath(__file__))
file_name = 'input_file.txt'

# This joins the script's folder with the filename
file_path = os.path.join(script_dir, file_name)

grid = []
with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
        row = line.strip()
        if row:
            grid.append(list(row))

rows = len(grid)
cols = len(grid[0])

# def check_adj(r, c):
#     directions = ((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1))
#     count = 0
#     for dr, dc in directions:
#             nr, nc = r + dr, c + dc

#             # Check if the neighbor is within the grid boundaries
#             if 0 <= nr < rows and 0 <= nc < cols:
#                 if grid[nr][nc] == '@':
#                     count += 1
#     return count

# TOTAL = 0
# # Part 1
# # for r in range(rows):
# #     for c in range(cols):
# #         if grid[r][c] == '@':
# #             if check_adj(r, c) < 4:
# #                 TOTAL += 1

# #Part 2
# FLAG = True

# while FLAG:

#     count = 0
#     for r in range(rows):
#         for c in range(cols):
#             if grid[r][c] == '@':
#                 if check_adj(r, c) < 4:
#                     grid[r][c] = '.'
#                     count += 1
#     if count == 0:
#         FLAG = False
#     TOTAL += count

# Cleaner approach
def get_neighbors(r, c):
    directions = ((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1))
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols:
            yield nr, nc

def count_adj(r, c):
    count = 0
    for nr, nc in get_neighbors(r, c):
        if grid[nr][nc] == '@':
            count += 1
    return count

# 1. Identify initial candidates
queue = deque()
for r in range(rows):
    for c in range(cols):
        if grid[r][c] == '@' and count_adj(r, c) < 4:
            queue.append((r, c))
            # Mark as 'queued' so we don't add the same roll twice
            grid[r][c] = 'X'

TOTAL = 0

# 2. Process the queue
while queue:
    r, c = queue.popleft()
    # Effectively remove the roll
    grid[r][c] = '.'
    TOTAL += 1

    # Only check neighbors of the roll we just removed
    for nr, nc in get_neighbors(r, c):
        if grid[nr][nc] == '@':
            if count_adj(nr, nc) < 4:
                queue.append((nr, nc))
                # Mark as 'queued' to prevent duplicates in the queue
                grid[nr][nc] = 'X'

if __name__ == "__main__":
    print(TOTAL)