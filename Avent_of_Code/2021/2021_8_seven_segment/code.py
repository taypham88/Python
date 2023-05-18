# Advent of Code
#--- Day 8: Seven Segment Search ---

pattern, output = [], []
with open('2021_8_seven_segment/input_file.txt') as file:

    for line in file:
        left, right = line.rstrip().split(' | ')

        pattern.append(left.split(' '))
        output.append(right.split(' '))

# part 1
count = 0
for string in output:
    for item in string:
        if len(item) in (2,4,3,7):
            count += 1
print(count)

# part 2
ans = 0
for i in range(len(pattern)):
    mapping = {}
    used = []
    for string in pattern[i]:
        if len(string) == 2:
            mapping['1'] = set(string)
            used.append(string)
        if len(string) == 3:
            mapping['7'] = set(string)
            used.append(string)
        if len(string) == 4:
            mapping['4'] = set(string)
            used.append(string)
        if len(string) == 7:
            mapping['8'] = set(string)
            used.append(string)
    for string in pattern[i]:
        if string not in used and len(string) == 6 and len(set(string).difference(mapping['1'])) == 5:
            mapping['6'] = set(string)
            used.append(string)
        if string not in used and len(string) == 5 and len(set(string).difference(mapping['1'])) == 3:
            mapping['3'] = set(string)
            used.append(string)
        if string not in used and len(string) == 6 and len(set(string).difference(mapping['4'])) == 3:
            mapping['0'] = set(string)
            used.append(string)
        if string not in used and len(string) == 6 and len(set(string).difference(mapping['4'])) == 2:
            mapping['9'] = set(string)
            used.append(string)
        if string not in used and len(string) == 5 and len(set(string).difference(mapping['4'])) == 3:
            mapping['2'] = set(string)
            used.append(string)
        if string not in used and len(string) == 5 and len(set(string).difference(mapping['4'])) == 2:
            mapping['5'] = set(string)
            used.append(string)

    temp =[]
    for string in output[i]:
        for k,v in mapping.items():
            if set(string) == v:
                temp.append(k)
    ans += int(''.join(temp))
print(ans)




