''''Video Length in Seconds'''
# You are given the length of a video in minutes. The format is mm:ss (ex: "02:54").
# Create a function that takes the video length and return it in seconds.
# Examples:
# minutesToSeconds("01:00") = 60
# minutesToSeconds("13:56") = 836
# minutesToSeconds("10:60") = -1
# minuteToSeconds("121:49") = 7309

def minutesToSeconds(inputstr):
    '''Seconds converstion with specific format'''
    mins, seconds = inputstr.split(':')

    try:
        imins = int(mins)
        isecs = int(seconds)
    except ValueError:
        print(f"Invalid Number {inputstr}")
        return -1

    if isecs >= 60:
        return -1

    return imins * 60 + isecs


if __name__=='__main__':
    print(minutesToSeconds("01:00"))
    print(minutesToSeconds("13:56"))
    print(minutesToSeconds("10:60"))
    print(minutesToSeconds("121:49"))
    print(minutesToSeconds("121:61"))
    print(minutesToSeconds("121:A9"))
    print(minutesToSeconds("AB0:49"))
