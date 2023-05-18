#--- Advent of code 2022 ---
#--- Day 4: Camp Cleanup ---

elf1 = []
elf2 = []
every,any = 0, 0
with open('2022_4_Camp/test.txt') as file:
    for line in file:
        left, right = line.rstrip().split(',')
        elf1.append(left.split('-'))
        elf2.append(right.split('-'))

for i in range(len(elf1)):
    item1 = set(range(int(elf1[i][0]),int(elf1[i][1])+1))
    item2 = set(range(int(elf2[i][0]),int(elf2[i][1])+1))
    # Part 1, totally overlap
    if item1.issubset(item2) or item2.issubset(item1):
        every += 1
    # Part 2 any elements
    if not item1.isdisjoint(item2) or not item2.isdisjoint(item1):
        any += 1
print('every',every)
print('any',any)



