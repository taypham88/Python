'''incrementing book problem and integer division'''
from timeit import timeit as timer
# integer division is the reverse of mod.

def incrementing(y):
    if y == 0:
        return 1
    if y % 2 == 1:
        return 2 * incrementing(y//2) # integer division is the assumption i was missing in the book.
    else:
        return y+1

print(timer('print(incrementing(0))', globals = globals(), number =100))