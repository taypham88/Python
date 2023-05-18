# hash_table ={
# 'CH':'B',
# 'HH':'N',
# 'CB':'H',
# 'NH':'C',
# 'HB':'C',
# 'HC':'B',
# 'HN':'C',
# 'NN':'C',
# 'BH':'H',
# 'NC':'B',
# 'NB':'B',
# 'BN':'B',
# 'BB':'N',
# 'BC':'B',
# 'CC':'N',
# 'CN':'C'}
# template = 'NNCB'

def parse_input(infile):
    template = infile.readline()
    next(infile)
    rules = {}
    for line in infile:
        left, right = line.split(' -> ')
        rules[left] = right.strip()
    return template, hash_table


with open('input_file.txt') as infile:
    template, hash_table = parse_input(infile)

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

for i in range(0, 2):
    temp = exp_poly(template, hash_table)
    template = temp

count_hash = {}

for i in template:
    if i not in count_hash:
        count_hash[i] = 1
    else:
        count_hash[i] += 1

print(max(count_hash.values())-min(count_hash.values()))
