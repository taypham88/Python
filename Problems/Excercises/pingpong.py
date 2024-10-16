'''Given an array of Ping!, create a function that inserts Pong! in between each element. Also:
If win equals true, end the list with Pong!
If win equals false, end the list with Ping!'''


def pingPong(arr, state):
    '''ping pong problem'''

    if not arr:
        return 'No Input Given'

    temp = []
    for i in range(len(arr)-1):
        temp.append(arr[i])
        temp.append('Pong!')

    temp.append(arr[-1])
    if state:
        temp.append('Pong!')

    return temp



if __name__ == '__main__':
    print(pingPong(["Ping!"], True))
    print(pingPong(["Ping!"], False))
    print(pingPong(["Ping!", "Ping!"], False))
    print(pingPong(["Ping!", "Ping!"], True))
    print(pingPong(["Ping!", "Ping!", "Ping!"], True))
    print(pingPong(["Ping!", "Ping!", "Ping!"], False))
    print(pingPong([], True))
