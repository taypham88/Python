
def isPalindrome(x : int):

    # :type x: int
    # :rtype: bool

    temp = x
    reverse = 0
    
    while x > 0:
        div = x % 10
        reverse = reverse * 10 + div
        x = x //10
        
    if temp == reverse:
        return True  
