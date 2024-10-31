#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    # Write your code here
    
    i = 0
    j = 0
    position = 0
    quantity = 0
    quantity_2 = 0
    result = []
    for i in range(len(a)):
        if a[position] > b[position]:
            quantity += 1 

        elif a[position] < b[position]:
            quantity_2 += 1
        position += 1
        
    print(quantity)
    print(quantity_2) 
    
    result.append(quantity)
    result.append(quantity_2)
    
    return(result)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
