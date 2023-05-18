# Advent of Code
#--- Day 4: Giant Squid ---

def parse_input(infile):
    numbers = [int(n) for n in infile.readline().strip().split(',')]
    next(infile)
    total_lines = []
    bingo_cards = {}
    count, next_card = 0, 1
    for line in infile:
        if line.strip().split(' ')== ['']:
            pass
        else:
            card = [i.replace(' ','') for i in line.strip().split(' ')]
            temp = []
            for i in card:
                if i != '':
                    temp.append(int(i))
            total_lines.append(temp)
    for line in total_lines:
        if next_card not in bingo_cards:
            bingo_cards[next_card] = []
            bingo_cards[next_card].append(line)
            count += 1
        else:
            bingo_cards[next_card].append(line)
            count += 1
        if count == 5:
            count = 0
            next_card += 1
    return numbers, bingo_cards

with open('2021_4_giant_squid/input_file.txt') as infile:
    numbers, bingo_cards= parse_input(infile)

# Part 1
class finish(Exception):
    pass

def find_in_set(subset, superset):
    if subset.issubset(superset):
        return True
    return False

# ans = -1
# val = float('inf')
# bingo_numbers = set(numbers[0:3])
# try:
#     for number in numbers[3:]:
#         bingo_numbers.add(number)
#         for k, v in bingo_cards.items():
#             for i in range(0,5):
#                 vert = set(v[i])
#                 hor = set([v[0][i],v[1][i],v[2][i],v[3][i],v[4][i]])

#                 if find_in_set(vert, bingo_numbers) or find_in_set(hor, bingo_numbers):
#                     ans, val = k, number
#                     raise finish
# except finish:
#     pass
# if ans != -1:
#     total = 0
#     for array in bingo_cards[ans]:
#         for num in array:
#             if num not in bingo_numbers:
#                 total += num
# print(total * val)

# Part 2
def find_score(k, bingo_cards):
    total = 0
    for array in bingo_cards[k]:
        for num in array:
            if num not in bingo_numbers:
                total += num
    return total

bingo_numbers = set(numbers[0:3])
completed = []
ans = []

for number in numbers[3:]:
    bingo_numbers.add(number)
    for k, v in bingo_cards.items():
        if k not in completed:
            for i in range(0,5):
                vert = set(v[i])
                hor = set([v[0][i],v[1][i],v[2][i],v[3][i],v[4][i]])

                if find_in_set(vert, bingo_numbers) or find_in_set(hor, bingo_numbers):
                    completed.append(k)
                    score = find_score(k, bingo_cards)*number
                    ans.append([k, number, score])

print(ans[-1])
