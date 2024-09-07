"""
Design a data structure that allows one to search, insert, and delete an integer  in  time
(i.e., constant time, independent of the total number of integers stored). Assume that  and that there are  units
of space available, where  is the maximum number of integers that can be in the table at any one time.
(Hint: use two arrays  and .) You are not allowed to initialize either  or , as that would take  or  operations.
This means the arrays are full of random garbage to begin with, so you must be very careful.
"""

def insert(A, B, x, k):

    k += 1
    A[x] = k
    B[k] = x
    return A, B, k

def search(A, B , x, k):

    return (A[x] < k) and (B[A[x]] == x)

def delete(A, B, x, k):

    A[B[k]] = A[x]
    B[A[x]] = B[k]
    k -= 1
    return A, B, k

if __name__ == '__main__':
    A =[1,3,4,5,2,4,5]
    B =[5, 2, 3, 2, 1]
    k = 0

    A, B, k = insert(A, B, 3, k)
    A, B, k = insert(A, B, 4, k)
    print(search(A, B, 3, k))
