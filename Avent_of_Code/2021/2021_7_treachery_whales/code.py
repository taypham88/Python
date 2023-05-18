# Advent of Code
#--- Day 7: The Treachery of Whales ---


crabs =[]

with open('2021_7_treachery_whales/input_file.txt') as infile:
    [crabs.append(int(x)) for x in infile.readline().split(',')]

# temp = []
# for i in crabs:
#     fuel = [abs(i-x) for x in crabs]
#     temp.append(sum(fuel))
# print(min(temp))

# Part 2 is each step cost that much fuel instead of 1
# Arithmetic sequence
def arithmetic_sum(start, end, n):
    ans = (n*(start + end))/2
    return ans

temp = []
for i in range(1,max(crabs)):
    fuel = [arithmetic_sum(1,abs(i-x), abs(i-x)) for x in crabs]
    temp.append(sum(fuel))
print(min(temp))