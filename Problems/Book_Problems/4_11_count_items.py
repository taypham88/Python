'''
Counts the occurrence of items in a list in linear time
'''

import numpy as np

def count(items):
    items.sort()
    counts = dict()
    for i in items:
        counts[i] = counts.get(i, 0) + 1
    return counts

if __name__ == '__main__':
    s1 = np.random.randint(10, size=100).tolist()
    print(count(s1))

