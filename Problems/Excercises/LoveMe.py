'''Sloth Challenge 8/28/2024'''

'''Given a number of petals, return a string which repeats the phrases "Loves me" and "Loves me not" for every
alternating petal, and return the last phrase in all caps. Remember to put a comma and space between phrases.'''

def lovesMe(n):
    if n <= 0:
        return ''
    if n == 1:
        return "LOVES ME"

    store = {0: "Loves me, ", 1: "Loves me not, ", 2: "LOVES ME", 3:"LOVES ME NOT"}

    ans = ''
    for i in range(n-1):
        if i % 2 == 0:
            ans += store[0]
        else:
            ans += store[1]

    if i % 2 == 1:
        ans += store[2]
    else:
        ans += store[3]

    return ans

if __name__ == '__main__':
    print(lovesMe(1))
    print(lovesMe(0))
    print(lovesMe(2))
    print(lovesMe(3))
    print(lovesMe(10))
