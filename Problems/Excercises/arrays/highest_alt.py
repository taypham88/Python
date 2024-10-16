'''
There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes.
The biker starts his trip on point 0 with altitude equal 0.

You are given an integer array gain of length n where gain[i] is the net gain in
altitude between points i​​​​​​ and i + 1 for all (0 <= i < n). Return the highest altitude of a point.
'''

def largestAltitude(gain):
    # start = [0]
    # new_alt =[0]
    # for i in range(0,len(gain)):
    #     new_alt.append(start[0]+gain[i])
    #     start[0] = start[0] + gain[i]
    # return max(new_alt)
# this works too and is superior
    ans,curr = 0,0
    for g in gain:
        curr+=g
        ans = max(ans,curr)
    return ans
gain = [-5,1,5,0,-7]
print(largestAltitude(gain))