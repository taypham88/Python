'''execution code for problem 3 of year 2023 advent of code'''
# Advent of Code
#--- Day 4: Scratchcards ---

import os
import collections


current_directory = os.getcwd()
file_name = 'input_file.txt'
file_path = os.path.join(current_directory, file_name)
PART1 = 0

with open(file_path, 'r') as file:
    CARDMAP = collections.defaultdict(int)

    for idx, line in enumerate(file):
        cards = line[7:].strip().split('|')
        WINSET, NUMSET = set(cards[0].split(' ')), set(cards[1].split(' '))
        WINSET.remove('')
        NUMSET.remove('')
        COMMONSET = WINSET.intersection(NUMSET)
        CARDMAP[idx+1] += 1

        if len(COMMONSET) != 0:
            for i in range(len(COMMONSET)):
                CARDMAP[idx+1+i+1] += CARDMAP[idx+1]
            PART1 += 2**(len(COMMONSET)-1)

PART2 = sum(CARDMAP.values())

print(PART1)
print(PART2)
