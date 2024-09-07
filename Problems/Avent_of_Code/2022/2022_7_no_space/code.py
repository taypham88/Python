#--- Advent of code 2022 ---
#--- Day 7: No Space Left On Device ---
from collections import deque

class Node:
    def __init__(self, name, size = 0):
        self.name = name
        self.size = size
        self.children = {}

    def __str__(self):
        return f"{self.name} {self.size}"

stack = deque()

with open('2022_7_no_space/input_file.txt') as file:
    for line in file:
        if "$ cd .." in line:
            stack.pop()
        elif "$ cd /" in line:
            temp = line.rstrip().split(' ')
            stack.append(Node(temp[-1]))
        elif "$ cd " in line:
            temp = line.rstrip().split(' ')
            newdir = Node(temp[-1])
            stack[-1].children[temp[-1]] = newdir
            stack.append(newdir)
        elif "$ ls" in line:
            pass
        elif "dir " in line:
            pass
        else:
            temp = line.rstrip().split(' ')
            stack[-1].children[temp[-1]] = Node(temp[-1], int(temp[0]))

def traverse(node, level = 0):
    print("  "*level + "- "+ str(node))

    for v in node.children.values():
        traverse(v, level + 1)

def get_size(node, dirSize):
    if not node.children: return node.size
    totalSize = 0
    for v in node.children.values(): totalSize += get_size(v,dirSize)
    dirSize.append(totalSize)
    return totalSize

myList =[]
# traverse(stack[0])
get_size(stack[0], myList)

# filtered = [num for num in myList if num <= 100000]
# print(sum(filtered))

# Part 2
minRequired = 30000000 - (70000000 - max(myList))
filtered = [num for num in myList if num >= minRequired]
print(min(filtered))