#--- Advent of code 2022 ---
#--- Day 5: Supply Stacks ---

test_table = {1: ['Z','N'],
              2: ['M', 'C', 'D'],
              3: ['P']}

input_table ={1: ['H', 'B', 'V', 'W', 'N', 'M', 'L', 'P'],
              2: ['M', 'Q', 'H'],
              3: ['N', 'D', 'B', 'G', 'F', 'Q', 'M', 'L'],
              4: ['Z', 'T', 'F', 'Q', 'M', 'W', 'G'],
              5: ['M', 'T', 'H', 'P'],
              6: ['C', 'B', 'M', 'J', 'D', 'H', 'G', 'T'],
              7: ['M', 'N', 'B', 'F', 'V', 'R'],
              8: ['P', 'L', 'H', 'M', 'R', 'G', 'S'],
              9: ['P', 'D', 'B', 'C', 'N']}

steps = []
with open('2022_5_supply/input_file.txt') as file:
    for line in file:
        line = line.rstrip().split(' ')
        temp =[]
        for index in range(len(line)):
            if index in (1,3,5):
                temp.append(int(line[index]))
        steps.append(temp)


# boxes, from , to /Part 1
# for moves in steps:
#     for i in range(moves[0]):
#         input_table[moves[2]].append(input_table[moves[1]].pop())

# Part 2
for moves in steps:
    temp = []
    for i in range(moves[0]):
        temp.append(input_table [moves[1]].pop())
    for i in range(moves[0]):
        input_table [moves[2]].append(temp.pop(-1))

# Part 1 what is the last letter of each column
for table in input_table .items():
    print(table)