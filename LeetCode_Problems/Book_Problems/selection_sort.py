'''
Book Chapter 2
selection sort problem page 42
selection sort is quadratic n^2

insertion sort problem page 43

'''
import time

def selection_sort(array):
    '''
    Find the min element in the remaining unsorted array
    '''
    init_time = time.time()

    for i in range(len(array)):
        min = i # index
        for j in range(i+1, len(array)):
            if array[min] > array[j]:
                min = j
        array[i], array[min] = array[min], array[i]

    print(f"selection sort time is {(time.time()-init_time)*1000:.4f}")

    return array

if __name__ == '__main__':

    A = [4,6,8,2,1,5,32,12,31,42,55,93,12,42,13,45,13]
    print(selection_sort(A))
