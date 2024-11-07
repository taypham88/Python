'''Given a sentence containing few instances of "Ctrl + C" and "Ctrl + V", return the sentence after those keyboard shortcuts have been applied!
"Ctrl + C" will copy all text behind it.
 "Ctrl + V" will do nothing if there is no "Ctrl + C" before it.
A "Ctrl + C" which follows another "Ctrl + C" will overwrite what it copies.'''

# Assumption no input Text can be #ACTIONCOPY# or #ACTIONPASTE#
def ctrlCV(arr):
    ans = []
    copied = []
    arr = arr.replace('Ctrl + C', '#ACTIONCOPY#')
    arr = arr.replace('Ctrl + V', '#ACTIONPASTE#')
    keys = arr.split(' ')
    for _,text in enumerate(keys):

        if text == '#ACTIONPASTE#':
            ans += copied
            copied = []

        elif text == '#ACTIONCOPY#':
            copied = ans
        else:
            ans.append(text)

    return ' '.join(ans)


if __name__=='__main__':
    print(ctrlCV('the egg and Ctrl + C Ctrl + V the spoon'))
    print(ctrlCV('WARNING Ctrl + V Ctrl + C Ctrl + V'))
    print(ctrlCV('The Ctrl + C Ctrl + V Town Ctrl + C Ctrl + V'))
