# Advent of Code
# --- Day 5: Hydrothermal Venture ---

def int_split(line):
    temp =[]
    for i in line:
        temp1 = []
        for number in i.split(','):
            temp1.append(int(number))
        temp.append(temp1)
    return temp

def parse_input(infile):
    matrix = []
    for line in infile:
        split = line.rstrip().split(' -> ')
        split2 = int_split(split)
        matrix.append(split2)
    return matrix

with open('2021_5_hydro_adventure/input_file.txt') as infile:
    matrix = parse_input(infile)

counter = 0
hash_t ={}
test = []
for [x1,y1],[x2,y2]in matrix:
    if x1 == x2:
        for y in range(min(y1,y2),max(y1,y2)+1):
            if ','.join([str(x1),str(y)]) not in hash_t:
                hash_t[','.join([str(x1),str(y)])] = 1
            else:

                hash_t[','.join([str(x1),str(y)])] += 1

    elif y1 == y2:
        for x in range(min(x1,x2),max(x1,x2)+1):
            if ','.join([str(x),str(y1)]) not in hash_t:
                hash_t[','.join([str(x),str(y1)])] = 1
            else:

                hash_t[','.join([str(x),str(y1)])] += 1
    else:
        x_slope = 1 if x2-x1 > 0 else -1
        y_slope = 1 if y2-y1 > 0 else -1
        diff_value = abs(x2-x1)
        # print(x1,y1,x2,y2)
        x, y = x1, y1

        for _ in range(diff_value+1):
            # print(x,y)
            if ','.join([str(x),str(y)]) not in hash_t:
                hash_t[','.join([str(x),str(y)])] = 1
            else:

                hash_t[','.join([str(x),str(y)])] += 1
            x += x_slope
            y += y_slope

counter = 0
for v in hash_t.values():
    if v > 1:
        counter += 1
print(counter)

