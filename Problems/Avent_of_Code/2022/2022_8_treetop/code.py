#--- Advent of code 2022 ---
#--- Day 8: Treetop Tree House ---

rows = {}
columns = {}
matrix = []
test = []

with open('2022_8_treetop/input_file.txt') as file:
    row = 0
    for line in file:
        matrix.append([int(num) for num in list(line.rstrip())])
        rows[row] = [int(num) for num in list(line.rstrip())]
        row += 1
        column = 0
        for num in list(line.rstrip()):
            if column not in columns: columns[column] = [int(num)]
            else: columns[column].append(int(num))
            column += 1

# Part 2
def scenic_score(row,column):
    left, right, top, bottom = 0, 0 , 0, 0

    for i in reversed(rows[row][:column]): #left
        left += 1
        if i >= matrix[row][column]: break
    for i in rows[row][column+1:]: #right
        right += 1
        if i >= matrix[row][column]: break
    for i in reversed(columns[column][:row]): # top
        top += 1
        if i >= matrix[row][column]: break
    for i in columns[column][row+1:]: # bottom
        bottom += 1
        if i >= matrix[row][column]: break

    return left*right*top*bottom

# for k,v in rows.items(): print(k,v)
# for k,v in columns.items(): print(k,v)

check = []
count = 0
maxx = 0
for row in range(len(matrix)):
    for column in range(len(matrix[row])):
        check = []
        if column > 0: # left
            if matrix[row][column] > max(rows[row][:column]): check.append(True)
        else: check.append(True)

        if column + 1 < len(matrix[row]): # right
            if matrix[row][column] > max(rows[row][column+1:]): check.append(True)
        else: check.append(True)

        if row > 0: # top
            if matrix[row][column] > max(columns[column][:row]): check.append(True)
        else: check.append(True)

        if row + 1 < len(matrix): # bottom
            if matrix[row][column] > max(columns[column][row+1:]): check.append(True)
        else: check.append(True)

        if True in check: maxx = max(maxx, scenic_score(row, column)); count += 1

print(count, maxx)
