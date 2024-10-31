#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    best = scores[0]
    worst = scores[0]
    bestTotal = 0
    worstTotal = 0
    
    for i in scores:
        if i < worst:
            worst = i
            worstTotal +=1
        elif i > best:
            best = i
            bestTotal += 1
            
    return[bestTotal, worstTotal]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
