'''
The mode of a bag of numbers is the number that occurs most frequently in the set. The set {4, 6, 2, 4, 3, 1} has a mode of 4.
Give an efficient and correct algorithm to compute the mode of a bag of  numbers.
'''

import numpy as np
import time
# using a dictionary is about twice as fast
def mode_of_list(list):
    init_time = time.time()
    list.sort()
    l = [0]
    results = []
    counter = 0
    for i in range(len(list)):
        if list[i] != l[0]:
            results.append([list[i-1], counter])
            new = list[i]
            l[0] = new
            counter = 1
        else:
            counter += 1
    print((time.time()-init_time)*1000)
    return max(results, key=lambda list:list[1])

def mode_of_list_dict(list):
    init_time = time.time()
    list.sort()
    freq = {}
    for item in list:
        if (item in freq):
            freq[item] += 1
        else:
            freq[item] = 1
    print((time.time()-init_time)*1000)
    return [max(freq, key=freq.get), max(freq.values())]

if __name__ == '__main__':
    y = np.random.randint(20, size=10000).tolist()
    results = mode_of_list_dict(y)
    print(results)
    results1 = mode_of_list(y)
    print(results1)