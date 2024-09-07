'''
4.20 Give an efficient algorithm to rearrange an array of n keys so that all the negative keys precede all the nonnegative keys.
Your algorithm must be in-place, meaning you cannot allocate another array to temporarily hold the items. How fast is your algorithm?
'''
import numpy as np

# pop and insert works but the below will not use extra memory and is inplace
def negative_sort(list):
    low, mid = 0, 0
    for mid in range(len(list)):
        if list[mid] < 0:
            list[mid], list[low] = list[low], list[mid]
            low += 1
            # a = list.pop(mid)
            # list.insert(0,a)
            print(f"test {list}")
    return list


if __name__ == '__main__':
    l =[]
    arr = np.random.randint(low =-5, high =5, size=10).tolist()
    print(arr)
    print(negative_sort(arr))