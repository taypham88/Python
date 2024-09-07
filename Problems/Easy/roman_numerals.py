"""Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer."""

string = ["III" , "LVIII", "MCMXCIV"]

"""class Solution(object):
    def romanToInt(self, s):

        roman = {'I': 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000, 'IV' : 4, 'IX': 9, 'XL': 40, 'XC' : 90, 'CD': 400, 'CM' : 900}
        count = 0
        number = 0
        
        while count < len(s):
            if count + 1 < len(s) and s[count : count + 2] in roman:
                number += roman[s[count: count + 2]]
                count += 2
            else:
                number += roman[s[count]]
                count += 1
        return number"""
  
class Solution(object):
    def romanToInt(self, s):
        d = {'I':1, 'V':5, 'X':10, 'L':50,'C':100,'D':500,'M':1000}
        number = 0 
        p = 0
        for i in range(len(s)-1,-1,-1):
            print(f"number is {number}")
            print(f"d[s[i]] is {d[s[i]]}")
            print(f"p is {p}")
            if d[s[i]]>= p:
                number += d[s[i]]
            else:
                number -= d[s[i]]
            p = d[s[i]]
        return number

      
ob1 = Solution()
#print(ob1.romanToInt("III"))
print(ob1.romanToInt("CDXLIII"))
#print(ob1.romanToInt(string[0]))
#print(ob1.romanToInt(string[1]))
#print(ob1.romanToInt(string[2]))
        


