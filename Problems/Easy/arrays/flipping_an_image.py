'''
Given an n x n binary matrix image, flip the image horizontally, then invert it, and return the resulting image.

To flip an image horizontally means that each row of the image is reversed.

For example, flipping [1,1,0] horizontally results in [0,1,1].
To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0.

For example, inverting [0,1,1] results in [1,0,0].
'''

def flipAndInvertImage(image):
    ans =[]
    l = len(image)
    for i in image:
        sub =[]
        for j in reversed(range(l)):
            if i[j] == 0:
                sub.append(1)
            else:
                sub.append(0)
        ans.append(sub)
    return ans

image = [[1,1,0],[1,0,1],[0,0,0]]
print(flipAndInvertImage(image))