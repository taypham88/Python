#--- Advent of code 2019---
#--- Day 1: The Tyranny of the Rocket Equation ---

from pathlib import Path

# Define the file path in a cross-platform way
project_root = Path(__file__).parent.parent
file_path = project_root / '2019_1_Tyranny' / 'input_file.txt'

with open(file_path, 'r',  encoding='utf-8') as file:
    TOTAL_FUEL = 0
    for num in file:
        temp = int(num.strip())
        curr = 0
        while temp > 0:
            temp = max(0,temp//3 - 2)
            curr += temp
        TOTAL_FUEL += curr

if __name__== '__main__':
    print(TOTAL_FUEL)