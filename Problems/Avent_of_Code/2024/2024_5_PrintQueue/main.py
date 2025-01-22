#--- Advent of code 2024---
#--- Day 5: Print Queue ---
import os
import collections

current_directory = os.getcwd()
file_name = 'test.txt'
file_path = os.path.join(current_directory, file_name)

ORDER = collections.defaultdict(list)
PAGES = []
with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
        if '|' in line:
            temp = line.strip().split('|')
            ORDER[temp[1]].append(temp[0])
        elif ',' in line:
            PAGES.append(line.strip().split(','))

TOTAL = 0

# part 1 function
# for job in PAGES:
#     compare_set = set(job)
#     current_set = set()

#     for page in job:
#         common_set = ORDER[page].intersection(compare_set)
#         common_set.difference_update(current_set)

#         if not common_set:
#             current_set.add(page)
#         else:

#             break
#     else:
#         TOTAL += int(job[len(job)//2])

'''Part 2'''
def topologicalSortUtil(v, visited, stack, graph):
    stack =[]

    # Mark the current node as visited.
    visited.add(v)
    # Recur for all the vertices adjacent to this vertex
    for i in graph[v]:
        if i not in visited and i in graph:
            topologicalSortUtil(i,visited,stack,graph)

    # Push current vertex to stack which stores result
    stack.insert(0,v)
    print(stack)
    return stack

for job in PAGES:

    visited = set()
    new_job = []
    for page in job:
        if page in ORDER:
            temp = topologicalSortUtil(page,visited,[],ORDER)
            print('temp')


    if new_job != job:
        TOTAL += int(new_job[len(new_job)//2])

print(TOTAL) # failing part 2
