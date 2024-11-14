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
        
        
    def search_wrong_number(rows, cols, magic_const):
        wrong_numbers = []
        for i in range(3):
            for j in range(3):
                if rows[i] < magic_const and cols[j] < magic_const:
                    wrong_numbers.append([i, j])
        return wrong_numbers
    
    
    def change_number(wrong_numbers, s, magic_const):
        
        for i in wrong_numbers:
            
            row = []
            col = []
        
            row_index = i[0]
            col_index = i[1]
            
            row = s[i[0]]
            col =[s[0][col_index], s[1][col_index], s[2][col_index]]
            
            
            def total(array, index):
                total = 0 
                for i in range(3):
                    if i == index:
                        break
                    total += array[i]
                return total
            
            total_row = total(row, row_index)
            fixed_number = magic_const - total_row
            cost = s[col_index][row_index] - fixed_number
            
            print(row, col)
            print(total_row, fixed_number)
                
            
            if cost < 0:
                return -1 * cost
            else:
                return cost
            '''
            row[row_index] = fixed_number
            col[col_index] = fixed_number
            '''
           
            
    '''     
    def fixer(fixed_numbers, wrong_numbers, s):
        
        for i in range(len(wrong_numbers)):
            row_index = wrong_numbers[i][0]
            col_index = wrong_numbers[i][1]
            
            s[col_index][row_index] = fixed_numbers
           
        return s
    '''
            
    rows = rowsCalc(s)
    cols = colsCalc(s)
    diagonal = diagonalCalc(s)
    wrong_numbers = search_wrong_number(rows, cols, magic_const)
    fixed_numbers = change_number(wrong_numbers, s, magic_const)
    #fixed_s = fixer(fixed_numbers, wrong_numbers, s)
    
    print("rows", rows)
    print("cols", cols)
    print("diagonal", diagonal)
    print("wrongs", wrong_numbers)
    print("fixed", fixed_numbers)
    #print("fixed s",fixed_s)
    
    return fixed_numbers
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()
