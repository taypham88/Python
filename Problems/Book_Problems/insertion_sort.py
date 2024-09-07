'''
Book Chapter 2

insertion sort problem page 43
since the inner loop goes around n times at most
it can be estimated as n^2

'''
import time

def insertion_sort(array):
    '''
    insertion sort, moves down the array and swaps until there are no more smaller numbers.
    '''

    init_time = time.time()

    for i in range(1,len(array)):
        key = array[i]
        j = i-1
        while j >= 0 and key < array[j]:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key
        print(array)

    print(f"insertion sort time is {(time.time()-init_time)*1000:.4f}")

    return array

if __name__ == '__main__':

    A = [4,6,8,2,1,5,32,12,31,42,55,93,12,42,13,45,13]
    print(insertion_sort(A))

