# Advent of Code
#--- Day 14: Extended Polymerization ---

def parse_input(infile):
    template = infile.readline()
    next(infile)
    hash_table = {}
    for line in infile:
        left, right = line.split(' -> ')
        hash_table[left] = right.strip()
    return template, hash_table

with open('2021_14_extended_polymer/input_file.txt') as infile:
    template, hash_table = parse_input(infile)

print(template, hash_table)

def exp_poly(poly, lookup):
    ans =''
    for i in range(len(poly)-1):
        pair = poly[i:i+2]

        if pair in lookup:
            temp = pair[0]+lookup[pair]
            ans += temp
        else:
            ans += pair[0]
    ans += poly[-1]

    return ans

for i in range(0, 40):
    temp = exp_poly(template, hash_table)
    template = temp

count_hash = {}
template = template.strip()

for i in template:
    if i not in count_hash:
        count_hash[i] = 1
    else:
        count_hash[i] += 1

print(max(count_hash.values())-min(count_hash.values()))
