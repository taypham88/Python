
# Advent of Code
# --- Day 2: Gift Shop ---

import os
from collections import deque

# This gets the directory where main.py is located
script_dir = os.path.dirname(os.path.abspath(__file__))
file_name = 'input_file.txt'

# This joins the script's folder with the filename
file_path = os.path.join(script_dir, file_name)

banks = []
with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
        banks.append(line.strip())

TOTAL = 0

# Part 1
# for bank in banks:
#     if len(bank) < 2:
#         continue

#     max_tens_digit = -1
#     best_bank_joltage = 0

#     for char in bank:
#         digit = int(char)

#         # If we've already seen a digit to the left,
#         # it could serve as the 'tens' place for the current 'digit'
#         if max_tens_digit != -1:
#             current_joltage = max_tens_digit * 10 + digit
#             if current_joltage > best_bank_joltage:
#                 best_bank_joltage = current_joltage

#         # Update the best candidate for the 'tens' place for future digits
#         if digit > max_tens_digit:
#             max_tens_digit = digit

#     TOTAL += best_bank_joltage

#Part 2
#monotonic stack

for bank in banks:

    l = len(bank) - 12
    stack = []

    for i, num in enumerate(bank):
        while stack and stack[-1] < num and l > 0:
            stack.pop()
            l -= 1
        stack.append(num)

    f_num = ''.join(stack[:12])
    TOTAL += int(f_num)

if __name__ == "__main__":
    print(TOTAL)