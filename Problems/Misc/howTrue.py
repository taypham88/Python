'''Create a function which returns the number of true values there are in an array.
Examples
countTrue([true, false, false, true, false]) ➞ 2

countTrue([false, false, false, false]) ➞ 0

countTrue([]) ➞ 0'''

def howTrue(arr: bool):
    
    if all(isinstance(item, bool) for item in arr):
        return sum(arr)

    print('invalid format')
    return 0

if __name__=='__main__':
    print(howTrue([True, False, True, False]))
    print(howTrue([False, False, False, False]))
    print(howTrue([True, True, True, True]))
    print(howTrue([]))
    print(howTrue([1,1,1,1]))
    print(howTrue([True,1,'1',1]))



