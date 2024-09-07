'''Simple excercise to create all permutations of a set of n characters'''
res = []
input_chars = ['A','B','C']
curr = []
def perm(chars):
    perms = [[]]
    for n in chars:
        print(n)
        nPerms = []
        for p in perms:
            print('selection', p)
            for i in range(len(p) + 1):
                print(len(p))
                pCopy = p.copy()
                pCopy.insert(i,n)
                print(pCopy)
                nPerms.append(pCopy)
        perms = nPerms
    return perms

if __name__ == '__main__':
    print(perm(input_chars))
