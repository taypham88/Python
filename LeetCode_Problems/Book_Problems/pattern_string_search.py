'''
match string search problem from book page 44
'''

def findmatch(string, txt):
    M = len(string)
    N = len(txt)

    for i in range(N-M+1):
        j = 0

        while (j < M):
            if (txt[i+j] != string[j]):
                break
            j += 1

        if (j == M):
            print(f'pattern found at index {i}')

if __name__ == '__main__':
    txt = "AABAACAADAABAAABAA"
    pat = "AABA"
    findmatch(pat, txt)