'''
4-9. Give an efficient algorithm to compute the union of sets A and B, where n=max(|A|,|B|).
The output should be an array of distinct elements that form the union of the sets, such that they
appear more than once in the union.
Assume that A and B are unsorted. Give an O(nlogn) algorithm for the problem.
Assume that A and B are sorted. Give an O(n) algorithm for the problem.
'''
import numpy as np

# lesson learned gotta watch for that while loop can't use <= with len() or it will index out.
def union(A , B):
    A = sorted(set(A))
    B = sorted(set(B))
    U = []
    i = 0
    j = 0
    while i < len(A) and j < len(B):
        if A[i] == B[j]:
            U.append(A[i])
            i +=1
            j +=1
        elif A[i] < B[j]:
            U.append(A[i])
            i +=1
        else:
            U.append(B[j])
            j +=1
    return U

if __name__ == '__main__':
    A = np.random.randint(20, size=100).tolist()
    B = np.random.randint(20, size=100).tolist()
    print(union(A,B))
