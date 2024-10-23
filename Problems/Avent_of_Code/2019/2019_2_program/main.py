#--- Advent of code 2019---
#--- Day 2: 1202 Program Alarm ---

from pathlib import Path
import itertools
# Define the file path in a cross-platform way
project_root = Path(__file__).parent.parent
file_path = project_root / '2019_2_program' / 'input_file.txt'

def computer(nums):
    i = 0
    while i < len(nums):
        if nums[i] == 99:
            break
        if nums[i] == 1:
            nums[nums[i+3]] = nums[nums[i+1]] + nums[nums[i+2]]
            i += 4
        if nums[i] == 2:
            nums[nums[i+3]] = nums[nums[i+1]] * nums[nums[i+2]]
            i+= 4
    return nums[0]

def find_noun_and_verb(nums):
    for noun, verb in itertools.product(range(100), repeat=2):
        copycode = nums.copy()
        copycode[1] = noun
        copycode[2] = verb
        if computer(copycode) == 19690720:
            print(noun, verb, 100 * noun + verb)
            return  # Exit the function immediately when found

if __name__== '__main__':
    with open(file_path, 'r',  encoding='utf-8') as file:
        for code in file:
            num = [int(x) for x in code.strip().split(',')]
            find_noun_and_verb(num)