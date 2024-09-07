'''
Write a function to perform integer division without using either the / or * operators.
Find a fast way to do it.
'''

def int_div(dividend, divisor):
    '''
    divides without using divider symbol.
    '''
    if divisor == 0:
        return 'can not divide by zero'
    sign = -1 if ((dividend < 0) ^ (divisor < 0)) else 1
    dividend = abs(dividend)
    divisor = abs(divisor)

    quotient = 0
    while dividend > divisor:
        dividend -= divisor
        quotient += 1

    if sign == -1:
        quotient = -quotient

    return quotient

if __name__ == '__main__':
    print(int_div(0,1))
    print(int_div(10,0))
    print(int_div(10,1))
    print(int_div(100,8))




