'''
Given a 6 x 6 2D Array, A:

	1 1 1 0 0 0
	0 1 0 0 0 0
	1 1 1 0 0 0
	0 0 0 0 0 0
	0 0 0 0 0 0
	0 0 0 0 0 0

We define an hourglass in A to be a subset of values with indices falling in this pattern in A's graphical representation:

a b c
  d
e f g
There are 16 hourglasses in A, and an hourglass sum is the sum of an hourglass' values.

Task: Calculate the hourglass sum for every hourglass in A, then print the maximum hourglass sum.

'''

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    glasses=[]
    for i in range(4):
        for j in range(4):
            glasses.append([arr[i][j:j+3],[0,arr[i+1][j+1],0],arr[i+2][j:j+3]])
    max_sum=-63
    for glass in glasses:
        tot=0
        for side in glass:
            tot+=sum(side)
        if tot>max_sum:
            max_sum=tot
        
    print(max_sum)
