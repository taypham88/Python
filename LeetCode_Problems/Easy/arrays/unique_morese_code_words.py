'''
International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows:

'a' maps to ".-",
'b' maps to "-...",
'c' maps to "-.-.", and so on.
For convenience, the full table for the 26 letters of the English alphabet is given below:

[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
Given an array of strings words where each word can be written as a concatenation of the Morse code of each letter.

For example, "cab" can be written as "-.-..--...", which is the concatenation of "-.-.", ".-", and "-...". We will call such a concatenation the transformation of a word.
Return the number of different transformations among all words we have.
'''

def uniqueMorseRepresentations(words):
    hash = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..'}
    # ans = set()
    # for word in words:
    #     newlist =[]
    #     for code in word:
    #         newlist.append(hash[code])
    #     ans.add(''.join(newlist))
    # return len(ans)

    morse = []
    count = 0

    for word in words:
        new_morse = ""
        for letter in word:
            new_morse += hash[letter.lower()]
        if new_morse not in morse:
            morse.append(new_morse)
            count += 1

    return count


words = ["gin","zen","gig","msg"]
print(uniqueMorseRepresentations(words))