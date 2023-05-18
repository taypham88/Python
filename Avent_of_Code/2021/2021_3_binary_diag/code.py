# Advent of Code
#--- Day 3: Binary Diagnostic ---

with open('2021_3_binary_diag/input_file.txt') as file:
    binary = [line.rstrip() for line in file]

# Part 1
# count ={}
# total = len(binary)
# for value in binary:
#     for i,v in enumerate(value):
#         if i not in count:
#             count[i] = int(v)
#         else:
#             count[i] += int(v)
# most = ''
# least =''
# for k,v in count.items():
#     if v > total/2:
#         most = most + '1'
#         least = least + '0'
#     else:
#         most = most + '0'
#         least = least + '1'

# print(int(most, base=2)*int(least, base=2))

# Part 2
def remove_bits(bin_input, index, ones):
    ans = []
    if ones:
        for value in bin_input:
            if value[index] == '1':
                ans.append(value)
    else:
        for value in bin_input:
            if value[index] == '0':
                ans.append(value)

    return ans

def common(bin_input, index, most_common):
    total = len(bin_input)
    count = 0
    for value in bin_input:
        count += int(value[index])
    if count > total/2:
        highest = '1'
    elif count < total/2:
        highest = '0'
    else:
        highest = 'tie'

    if most_common:
        if highest == '1':
            var = True
        elif highest == '0':
            var = False
        else:
            var = True
    else:
        if highest == '1':
            var = False
        elif highest == '0':
            var = True
        else:
            var = False
    ans = remove_bits(bin_input, index, var)

    return ans

oxy_rating = binary
co2_scrub = binary

for i in range(0,12):
    if len(oxy_rating) == 1:
        break
    else:
        oxy_rating = common(oxy_rating, i, True)

for i in range(0,12):
    if len(co2_scrub) == 1:
        break
    else:
        co2_scrub = common(co2_scrub, i, False)

print(int(oxy_rating[0], base = 2) * int(co2_scrub[0], base = 2))
