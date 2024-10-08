'''
Write a function that converts a sentence into pig latin.
Rules for converting to pig latin:
For words that begin with a vowel (a, e, i, o, u), add "way".
Otherwise, move all letters before the first vowel to the end and add "ay".
For simplicity, no punctuation will be present in the inputs.

#Example 1
pigLatinSentence("this is pig latin")
output = "isthay isway igpay atinlay"

#Example 2
pigLatinSentence("wall street journal")
output = "allway eetstray ournaljay"
'''

def piglatin(string):
    '''
    Assumptions:
    # uppercase letters will remain the same case when reordered.
    # y added as a special rule in pig latin for letters other than the first.
    # numbers and orther characters treated as words.`
    '''
    ans = ''
    if not string or not string.strip():
        return ans

    vowels = {'a', 'e', 'i', 'o', 'u'}

    for word in string.split(' '):
        if word[0].lower() in vowels:
            ans += word + 'way '
            continue

        has_vowel = False
        for i,v in enumerate(word):
            if v.lower() in vowels or v.lower() == 'y':
                ans += word[i:] + word[:i] + 'ay '
                has_vowel = True
                break

        if not has_vowel:
            ans += word + 'ay '

    return ans.strip()

if __name__ == '__main__':
    print(piglatin("This is pig latin"))
    print(piglatin("Wall street journal"))
    print(piglatin("Hmmm there is a fly in my shh"))
    print(piglatin(" "))
    print(piglatin(""))
    print(piglatin('1 223, 44'))