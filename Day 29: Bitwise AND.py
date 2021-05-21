'''

Task
Given set S = {1,2,3,..,N}. Find two integers, A and B (where A < B), from set S such that the value of A&B is the maximum possible and also less than a given integer,K . 
In this case, & represents the bitwise AND operator.

Function Description
Complete the bitwiseAnd function in the editor below.

bitwiseAnd has the following paramter(s):
- int N: the maximum integer to consider
- int K: the limit of the result, inclusive

Returns
- int: the maximum value of A&B within the limit.

'''

!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bitwiseAnd' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER N
#  2. INTEGER K
#


def max_bit(n,k):
    maximum = 0
    for i in range(1,n+1):
        for j in range(1,i):
            h = i & j
            if maximum < h < k:
                maximum = h
            if maximum == k-1:
                return maximum
    return maximum

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])
        
        print(max_bit(n,k))
