#! /usr/bin/env python3
#Note: Try to solve this task in-place (with O(1) additional memory), since this is what you'll be asked to do during an interview.
#You are given an n x n 2D matrix that represents an image. Rotate the image by 90 degrees (clockwise).
#
# Orig
#   [[1, 2, 3],
#    [4, 5, 6],
#    [7, 8, 9]]
#
# 90 deg
#    [[7, 4, 1],
#     [8, 5, 2],
#     [9, 6, 3]]



def rotateImage(a):
    #print(a)
    b = []
    for j in range(len(a)):
        c = []
        for i in reversed(range(len(a))):
            c.append(a[i].pop(0))
        b.append(c)
    return(b)

#testimg = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
testimg = [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12],[13, 14, 15, 16]]

print(rotateImage(testimg))
