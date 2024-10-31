#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    new_arr = sorted(arr)
    max_len = []
    '''
    for i in new_arr:
        count = 1
        for j in new_arr:
            if i == j:
                count+=1
            else:
                max_len.append([i,count])
                break
    '''
    
    count = 0
    for i in range(len(new_arr) - 1):  
        actual = new_arr[i]
        siguiente = new_arr[i + 1]
        if actual == siguiente: 
            count+=1
        if actual != siguiente or i == len(new_arr)-2:
            #print(new_arr[i],i,'added')
            max_len.append([actual,count+1])
            count = 0
    for i in max_len:
        print(i[1])
    array_ordenado = sorted(max_len, key=lambda x: x[1], reverse=True)
    print(array_ordenado)
    return array_ordenado[0][0]
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
