'''execution code for problem 3 of year 2023 advent of code'''
# Advent of Code
# --- Day 1: Secret Entrance ---

import os

# This gets the directory where main.py is located
script_dir = os.path.dirname(os.path.abspath(__file__))
file_name = 'test.txt'

# This joins the script's folder with the filename
file_path = os.path.join(script_dir, file_name)

steps = []
with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
            line = line.strip()
            if not line: continue
            val = int(line[1:])
            steps.append(val if line[0] == 'R' else -val)
#part 1
# def count_zeros(moves):
#     curr = 50
#     print(curr)
#     count = 0
#     for move in moves:
#         curr = (curr + move) % 100
#         print(curr)
#         if curr == 0:
#             count += 1
#     return count

# 2. Count the Zeros
def crossings(moves):
    curr = 50
    total_zeros = 0

    for move in moves:
        # We check every 'click' in the rotation
        if move > 0: # Moving Right
            for _ in range(move):
                curr = (curr + 1) % 100
                if curr == 0:
                    total_zeros += 1
        else: # Moving Left
            for _ in range(abs(move)):
                curr = (curr - 1) % 100
                if curr == 0:
                    total_zeros += 1

    return total_zeros
#math only solution
def count_all_zeros(moves):
    curr = 50
    total_zeros = 0

    for move in moves:
            if move == 0:
                continue

            if move > 0:
                # Right: How many multiples of 100 are in the range (curr, curr + move]
                # We use (curr + move) // 100 because the boundary is at the end of the step
                total_zeros += (curr + move) // 100 - (curr // 100)
                print((curr + move) // 100 - (curr // 100), move)
            else:
                # Left: How many multiples of 100 are in the range [curr + move, curr)
                # We subtract 1 from the positions to align the "zero" correctly for left movement
                total_zeros += (curr - 1) // 100 - ((curr + move - 1) // 100)
                print((curr - 1) // 100 - ((curr + move - 1) // 100), move)

            # Update current position
            curr = (curr + move) % 100

    return total_zeros

if __name__ == "__main__":
    x = count_all_zeros(steps)
    print(x)