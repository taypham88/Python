# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.

class Solution(object):
    def maxArea(self, height):
        
        # ans = 0
        # for l in range(len(height)):
        #     for r in range(l + 1, len(height)):
        #         area = (r - 1) * min(height[l],height[r])
        #         print(area)
        #         ans = max(ans, area)
        # return ans

        ans = 0
        l, r = 0, len(height)-1
        while l < r:
            if height[l] < height[r]:
                min_height = height[l]
                min_index = l
            else:
                min_height = height[r]
                min_index = r
            ans = max(ans, (r - l) * min_height)
            if l + 1 == min_index +1:
                l += 1
            else:
                r -=1
        return ans


obi = Solution()
print(obi.maxArea([1,1]))
print(obi.maxArea([1,8,6,2,5,4,8,3,7]))

# best answer:
# class Solution(object):
#     def maxArea(self, height):

#         tallest = max(height)
#         i, best, breaker = 0, 0, 0
#         j = len(height) - 1
#         while i < j:
#             x = height[i]
#             y = height[j]
#             base = j - i

#             if base < breaker: # base must be > best / tallest
#                 return best #breaker breaker one nine

#             if x > y:
#                 area = base * y
#                 while (i < j) and (height[j] <= y): #find next biggest from the rite
#                     j -= 1
#             else:
#                 area = base * x
#                 while (i < j) and (height[i] <= x): #find next biggest from the laft
#                     i += 1

#             if area >= best: #update if better obv
#                 best = area
#                 breaker = (best / tallest)

#             if i == j: #meet in the middle
#                 return best
#         return best