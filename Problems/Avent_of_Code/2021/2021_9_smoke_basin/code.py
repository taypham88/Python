# Advent of Code
#--- Day 9: Smoke Basin ---

def spiral_recursion(level, i, checked):

    if output[level][i] >= 9:
        return
    else:
        if [level+1,i] not in checked and level+1 < len(output):
            top = output[level+1][i]
            if top < 9:
                checked.append([level+1,i])
                spiral_recursion(level+1,i,checked)
        if [level-1,i] not in checked and level-1 > -1:
            bottom = output[level-1][i]
            if bottom < 9:
                checked.append([level-1,i])
                spiral_recursion(level-1,i,checked)
        if [level,i+1] not in checked and i+1 < len(output[level]):
            right = output[level][i+1]
            if right < 9:
                checked.append([level,i+1])
                spiral_recursion(level,i+1, checked)
        if [level,i-1] not in checked and i-1 > -1:
            left = output[level][i-1]
            if left < 9:
                checked.append([level,i-1])
                spiral_recursion(level,i-1, checked)

with open('2021_9_smoke_basin/input_file.txt') as infile:
    output = []
    for line in infile:
        temp = []
        for item in line.rstrip():
            temp.append(int(item))
        output.append(temp)

checked = []
#part 1, just add up all the low points. Part 2 i have to use recursion or queues after finding the low spot.
for level in range(len(output)):
    for i,v in enumerate(output[level]):
        temp =[]
        if level-1 > -1:
            temp.append(output[level-1][i])

        if i-1 > -1:
            temp.append(output[level][i-1])

        if i+1 < len(output[level]):
            temp.append(output[level][i+1])

        if level+1 < len(output):
            temp.append(output[level+1][i])

        test = [v < i for i in temp]

        if False not in test:
            checked.append([level,i])

ans = []
for point in checked:
    temp = []
    spiral_recursion(point[0], point[1], temp)
    ans.append(len(temp))
ans.sort()
topScores = ans[len(ans)-2:]
res = ans[len(ans)-3]
for i in topScores:
    res = res * i
print(res)