#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    def __init__(self, s, t, a, b, apples, oranges):
        self.s = s
        self.t = t 
        self.a = a 
        self.b = b 
        self.apples = apples
        self.oranges = oranges
    
    def Distance(x, fruits):
        realDistance = []
        for i in fruits:
            realPlus = x + i
            realDistance.append(realPlus) 
        return(realDistance)
    start = s
    end = t
    
    
    def Match(fruits):
        counter = 0
        for i in fruits:
            if i >= start and i <= end:
                counter+=1

        return(counter)
                 
    applesDistance = Distance(a, apples)
    orangeDistance = Distance(b, oranges)
    I = Match(applesDistance)
    T = Match(orangeDistance)
    print(I)
    print(T)
    

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
