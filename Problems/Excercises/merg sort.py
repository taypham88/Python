
Y = [7,1,5,6,2,4,9,3]

def merge_sort(A, a = 0, b = None):
    # print('merge sort')
    if b is None: b = len(A)
    # print(f"A is {A}")
    # print(f"a is {a}")
    # print(f"b is {b}")
    # print(1 < b - a)
    if 1 < b - a:
        c = (a + b +1) // 2
        # print(f"c is {c}")
        merge_sort(A, a, c)
        merge_sort(A, c, b)
        L, R = A[a:c], A[c:b]
        # print(f"L is {L}")
        # print(f"R is {R}")
        merge(L, R, A, len(L), len(R), a, b)

def merge(L, R, A, i, j, a, b):
    # print('merge activate')
    # print(f"A is {A}")
    # print(f"a is {a}")
    # print(f"b is {b}")
    # print(f"L is {L}")
    # print(f"R is {R}")
    # print(f"i is {i}")
    # print(f"j is {j}")
    # print(f"L matrix is {L[i - 1]}")
    # print(f"R matrix is {R[j - 1]}")
    # print((j <= 0) or (i > 0 and L[i - 1] > R[j - 1]))
    if a < b:
        if (j <= 0) or (i > 0 and L[i - 1] > R[j - 1]):
            A[b - 1] = L[i - 1]
            i = i - 1
        else:
            A[b - 1] = R[j - 1]
            j = j - 1
        merge(L, R, A, i, j, a, b - 1)
        
        
        
merge_sort(Y)
print(f"Final Y is {Y}")