'''
 Assume that we are given  pairs of items as input, where the first item is a number and the second item is one of three colors
 (red, blue, or yellow). Further assume that the items are sorted by number. Give an  algorithm to sort the items by color
 (all reds before all blues before all yellows) such that the numbers for identical colors stay sorted.
For example: (1,blue), (3,red), (4,blue), (6,yellow), (9,red) should become (3,red), (9,red), (1,blue), (4,blue), (6,yellow).
'''
# bucket sort in linear time means for loops.
def stable_sort(x):
    red = []
    blue = []
    yellow = []
    for i in range(len(x)):
        if x[i][1] == 'red':
            red.append(x[i])
        if x[i][1] == 'blue':
            blue.append(x[i])
        if x[i][1] == 'yellow':
            yellow.append(x[i])
    return red + blue + yellow

if __name__ == '__main__':
    p = [(1,'blue'), (3,'red'), (4,'blue'), (6,'yellow'), (9,'red')]
    l = stable_sort(p)
    print(l)
