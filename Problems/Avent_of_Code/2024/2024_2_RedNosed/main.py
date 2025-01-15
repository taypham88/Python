#--- Advent of code 2024---
#--- Day 2: Red-Nosed Reports ---

import os

def inc_dec_check(arr):
    inc, dec = True, True

    # check difference
    for i in range(1,len(arr)):
        if abs(arr[i-1] - arr[i]) > 3 or arr[i-1] == arr[i]:
            return False

    # Check increasing
    for i in range(1,len(arr)):
        if arr[i-1] > arr[i]:
            inc = False
            break

    # Check decreasing
    for i in range(1,len(arr)):
        if arr[i-1] < arr[i]:
            dec = False
            break

    return inc or dec

current_directory = os.getcwd()
file_name = 'input.txt'
file_path = os.path.join(current_directory, file_name)

first, second = [],[]
SAFE = 0
with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
        temp = [int(x) for x in line.split()]
        if inc_dec_check(temp):
            SAFE += 1
        else:
            # Added for part 2. Treis them all
            for idx in range(len(temp)):
                arr = temp.copy()
                del arr[idx]
                if inc_dec_check(arr):
                    SAFE += 1
                    break

print(SAFE)
