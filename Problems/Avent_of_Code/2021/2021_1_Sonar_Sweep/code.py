# Advent of Code
#--- Day 1: Sonar Sweep ---


with open('2021_1_Sonar_Sweep/input_file.txt') as file:
    sonar = [int(line.rstrip()) for line in file]
# part 1 simple comparison
# first = sonar[0]
# count = 0
# for i in range(1, len(sonar)):
#     second = sonar[i]
#     diff = second - first
#     if diff > 0:
#         count +=1
#     first = second

# print(count)

# part 2: sliding scale
damp = []
for i in range(len(sonar) -2):
    damp.append(sonar[i]+sonar[i+1]+sonar[i+2])
first = damp[0]
count = 0
for i in range(1, len(damp)):
    second = damp[i]
    diff = second - first
    if diff > 0:
        count +=1
    first = second

print(count)
