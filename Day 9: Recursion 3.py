# Complete the factorial function in the editor below. Be sure to use recursion.
# factorial has the following paramter:
#     int n: an integer
# Returns
#     int: the factorial of 
# Note: If you fail to use recursion or fail to name your recursive function factorial or Factorial, you will get a score of ).

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the factorial function below.
def factorial(n):
    if n == 1:
        return n
    else: 
        return n * factorial(n-1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = factorial(n)

    fptr.write(str(result) + '\n')

    fptr.close()
