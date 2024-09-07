# Advent of Code
#--- Day 6: Lanternfish ---

fish =[]

with open('2021_6_Lantern_fish/input_file.txt') as infile:
    [fish.append(int(x)) for x in infile.readline().split(',')]

days = 256

# for _ in range(days):
#     newfish = 0
#     for i in range(len(fish)):
#         fish[i] -= 1
#         if fish[i] == -1:
#             fish[i] = 6
#             newfish += 1
#     for _ in range(newfish):
#         fish.append(8)

# print(len(fish))

# Part 2 is to run it on 256 days which is too large.


cache ={}

def compute(days):
    # check cache for resutls
    if days in cache:
        return cache[days]

    # check for base case
    if days <= 0:
        return 0

    # compute results and store in cache
    gens = (days-1)//7
    count = 0
    for i in range(gens+1):
        count += 1 + compute(days-i*7-9)
    cache[days] = count
    return count

counter = 0
for timer in fish:
    counter += compute(days - timer)

print(counter + len(fish))



