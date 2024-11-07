#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#

def formingMagicSquare(s):
    
    magic_const = 15
    
    def rowsCalc(s):
        rows = []
        for i in s:
            rows.append(i[0]+i[1]+i[2])
        return rows
            
    def colsCalc(s):
        cols = []
        for i in range(3):
            cols.append(s[0][i]+s[1][i]+s[2][i])
        return cols
        
    def diagonalCalc(s):
        diagonal = []
        diagonal.append(s[0][0]+s[1][1]+s[2][2])
        return diagonal

    rows = rowsCalc(s)
    cols = colsCalc(s)
    diagonal = diagonalCalc(s)
    
    print("rows", rows)
    print("cols" ,cols )
    print("diagonal", diagonal)
    
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()
