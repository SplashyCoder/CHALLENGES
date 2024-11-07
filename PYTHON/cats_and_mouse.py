#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    cat_a = z-x
    cat_b = z-y
    
    if cat_a < 0:
        cat_a = -1 * cat_a
    if cat_b < 0:
        cat_b = -1 * cat_b
    
    print('cat_a',{cat_a})
    print(' cat_b',{cat_b})
    if cat_a == cat_b:
        return(str('Mouse C'))
    if cat_a > cat_b:
        return(str('Cat B'))
    if cat_a < cat_b:
        return(str('Cat A'))
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        fptr.write(result + '\n')

    fptr.close()
