#!/bin/python3

import math
import os
import random
import re
import sys
import functools as fc
#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    list_sorted = lambda arr: list(set(sorted(arr)))
    a_new = list_sorted(a)
    b_new = list_sorted(b)
    total = 0
    
    for i in range(a_new[-1],b_new[0]+1):
        is_factor = True
        
        for factor in a:
            if i % factor !=  0:
                is_factor = False
                break
        
        for multiple in b:
            if multiple % i:
                is_factor = False
                break
        if is_factor == True:
            total += 1
    return total
        


        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
