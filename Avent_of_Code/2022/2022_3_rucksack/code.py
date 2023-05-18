#--- Advent of code 2022 ---
#--- Day 3: Rucksack Reorganization ---

priority = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15,
        'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26, 'A': 27, 'B': 28, 'C': 29,
        'D': 30, 'E': 31, 'F': 32, 'G': 33, 'H': 34, 'I': 35, 'J': 36, 'K': 37, 'L': 38, 'M': 39, 'N': 40, 'O': 42, 'P': 42, 'Q': 43,
        'R': 44, 'S': 45, 'T': 46, 'U': 47, 'V': 48, 'W': 49, 'X': 50, 'Y': 51, 'Z': 52}

left, right = [], []
with open('2022_3_rucksack/test.txt') as file:
    for line in file:
        line = line.rstrip()
        left.append(line[:len(line)//2])
        right.append(line[len(line)//2:])

# Part 1
# ans = 0
# for i in range(len(left)):
#     temp = ''.join(set(left[i]).intersection(set(right[i])))
#     ans += priority[temp]
# print(ans)

# Part 2
ans = 0
for i in range(0,len(left), 3):
    temp1 = set(left[i] + right[i])
    temp2 = set(left[i+1] + right[i+1])
    temp3 = set(left[i+2] + right[i+2])
    lookup = ''.join(temp1.intersection(temp2,temp3))
    ans += priority[lookup]
print(ans)


