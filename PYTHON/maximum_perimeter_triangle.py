#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    # Write your code here
        
    for numero in range(1,n+1):
        star = []
        for i in range(0,numero):
            star.append('#')
        text = ''.join(star)
        print(text.rjust(n))

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
