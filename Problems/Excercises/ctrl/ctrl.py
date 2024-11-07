'''Given a sentence containing few instances of "Ctrl + C" and "Ctrl + V", return the sentence after those keyboard shortcuts have been applied!
"Ctrl + C" will copy all text behind it.
 "Ctrl + V" will do nothing if there is no "Ctrl + C" before it.
A "Ctrl + C" which follows another "Ctrl + C" will overwrite what it copies.'''

# Assumption is that all Ctrl strings are only Ctrl + C or Ctrl + V.
# For example Ctrl + X would not be possible.
def ctrlCV(arr):
    ans = []
    copied = []
    keys = arr.split(' ')
    for i,v in enumerate(keys):
        if v in ('+', 'V', 'C'):
            continue
        if v == 'Ctrl':
            if copied and keys[i+2] == 'V':
                ans += copied
                copied = []
            elif keys[i+2] == 'C':
                copied = ans
        else:
            ans.append(v)
    return ans


if __name__=='__main__':
    print(ctrlCV('the egg and Ctrl + C Ctrl + V the spoon') == ['the', 'egg', 'and', 'the', 'egg', 'and', 'the', 'spoon'])
    print(ctrlCV('WARNING Ctrl + V Ctrl + C Ctrl + V'))
    print(ctrlCV('The Ctrl + C Ctrl + V Town Ctrl + C Ctrl + V'))
