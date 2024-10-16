'''
You are given an array rectangles where rectangles[i] = [li, wi] represents the ith rectangle of length li and width wi.

You can cut the ith rectangle to form a square with a side length of k if both k <= li and k <= wi. For example, if you have a rectangle [4,6], you can cut it to get a square with a side length of at most 4.

Let maxLen be the side length of the largest square you can obtain from any of the given rectangles.

Return the number of rectangles that can make a square with a side length of maxLen.
'''

def countGoodRectangles(rectangles):
    count ={}
    for rectangle in rectangles:
        if count.get(min(rectangle)) is None:
            count[min(rectangle)] = 1
        else:
            count[min(rectangle)] = count[min(rectangle)] + 1
    return count[max(count)]

# or can just use .count
    # squares = [min(rectangle[0], rectangle[1]) for rectangle in rectangles]
    # return squares.count(max(squares))

rectangles = [[5,8],[3,9],[3,12]]
print(countGoodRectangles(rectangles))