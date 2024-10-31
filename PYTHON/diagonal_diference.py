#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    def diagonal (arr):
        primary = 0
        
        i = 0 
        j = 0 
        
        while i < len(arr):
            primary += arr[i][j]
            i += 1
            j += 1
        return(primary)
  
    backWards_arr = []
    for i in reversed(arr):
        backWards_arr.append(i)

    return(abs(diagonal(arr)-diagonal(backWards_arr)))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
