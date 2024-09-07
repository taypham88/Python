#--- Advent of code 2022 ---
#--- Day 9: Rope Bridge ---

moves = []
with open('2022_9_rope/input_file.txt') as file:
    for line in file:
        temp = line.rstrip().split(' ')
        moves.append([temp[0],int(temp[1])])

# Part 1
# Starting positions [x,y] x is right left coordinate, y is up down coordinate

head = [0,0]
tail = [[0,0] for _ in range(9)]
tailVisited = [[[0,0]] for _ in range(9)]
lookup = {'U':[1,1], 'D':[1,-1], 'R':[0,1], 'L':[0,-1]}

for move in moves:
    temp = lookup[move[0]]
    for i in range(move[1]):

        head[temp[0]] += temp[1]
        distance = list(head)

        for i in range(len(tail)):
            distance_x = distance[0] - tail[i][0]
            distance_y = distance[1] - tail[i][1]
            if not (abs(distance_x) <=1 and abs(distance_y) <= 1):
                # always will be negative or positive given the input int(abs(x)/x)
                if distance_x != 0: tail[i][0] += int(abs(distance_x)/distance_x)
                if distance_y != 0: tail[i][1] += int(abs(distance_y)/distance_y)
            distance = tail[i]
            if list(distance) not in tailVisited[i]:
                tailVisited[i].append(list(distance))

print(len(tailVisited[8]))
