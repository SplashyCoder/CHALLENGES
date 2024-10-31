#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    divide = len(arr)
    negative = 0
    positive = 0 
    neutral = 0
    for i in arr:
        if i < 0:
            negative +=1
        elif i > 0:
            positive +=1
        else:
            neutral +=1

    negative_total = negative/divide
    positive_total = positive/divide 
    neutral_total = neutral/divide
    print ("{0:.6f}".format(positive_total))
    print ("{0:.6f}".format(negative_total))
    print ("{0:.6f}".format(neutral_total))
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
