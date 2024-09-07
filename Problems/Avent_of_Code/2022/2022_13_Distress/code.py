#--- Advent of code 2022 ---
#--- Day 13: Distress Signal ---

left, right = [],[]
data = open('2022_13_Distress/input_file.txt').read().strip()

for group in data.split('\n\n'):
    temp1,temp2 = group.split('\n')
    left.append(eval(temp1))
    right.append(eval(temp2))

def compare(left,right):
    if isinstance(left, int) and isinstance(right, int):
        if left > right:
            return False
        elif left == right:
            return None
        else:
            return True
    elif isinstance(left, list) and isinstance(right, list):
        i = 0
        while i < len(left) and i < len(right):
            ans = compare(left[i],right[i])
            if ans == True:
                return True
            if ans == False:
                return False
            i += 1
        if len(left) > len(right):
            return False
        elif len(left) < len(right):
            return True
        else:
            return None
    elif isinstance(left, int) and isinstance(right, list):
        return compare([left],right)
    else:
        return compare(left,[right])

res = 0
for i in range(len(left)):
    temp = compare(left[i],right[i])
    if temp == True:
        res += i+1

# print(res)

# Part 2
total = left + right + [[2]] + [[6]]

n = len(total)
for i in range(n):
    for j in range(n - i - 1):
        if not compare(total[j], total[j+1]):
            total[j], total[j+1] = total[j+1], total[j]

print((total.index([2])+1) * (total.index([6])+1))


