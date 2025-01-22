'''
Create a function that takes a string and censors words over four characters with *.
Examples
censor("The code is fourty")
output = "The code is ******"

censor("Two plus three is five")
output = "Two plus ***** is five"

censor("aaaa aaaaa 1234 12345")
output = "aaaa ***** 1234 *****"
'''


def censor_word(word):
    temp = word.strip().split(' ')
    ans = []

    for item in temp:
        if len(item) > 4:
            ans.append('*'*len(item))
        else:
            ans.append(item)
    return ' '.join(ans)

if __name__ == '__main__':
    print(censor_word("The code is fourty"))
    print(censor_word("Two plus three is five"))
    print(censor_word("aaaa aaaaa 1234 12345"))
    print(censor_word("      "))
    print(censor_word(""))