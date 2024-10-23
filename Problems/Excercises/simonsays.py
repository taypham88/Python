'''Simon asks you to perform operations on a list of numbers that only he tells you.
You should ignore all other instructions given.
Create a function which evaluates a list of commands (written in plain English) if the command begins with Simon says. Return the result as an integer.'''

def add(int1,int2):
    return int1 + int2

def subtract(int1,int2):
    return int1 - int2

def multiply_numbers(int1,int2):
    return int1 * int2

lookup = {'add': add, 'subtract':subtract, 'multiply': multiply_numbers}

def simons(arr):
    TEMP = 0
    for sentence in arr:
        sentence = list(sentence.split(' '))
        if sentence[0] == "Simon" and sentence[1] == 'says':
            TEMP = lookup[sentence[2]](TEMP,int(sentence[-1]))
    return TEMP

if __name__== '__main__':
    print(simons(["Simon says add 4", "Simon says add 6", "Then add 5"]))
    print(simons(["Susan says add 10","Simon says add 3","Simon says multiply by 8"]))
    print(simons(["Firstly, add 4","Simeon says subtract 100"]))
