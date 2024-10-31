#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
        flag = True
        aux_prim = 0
        for i in arr:
            aux_prim = aux_prim + i
        
        if aux_prim/i == i:
            flag = False
            print(f'{i*4} {i*4}')
        
        sumas = []
        resultados = []
        for i in arr:
            for j in arr:
                if i != j:
                    sumas.append(j)                
            sumas.append(".")
            
        aux = 0
        for i in sumas:
            if i != '.':
                aux = aux + i
            else:
                resultados.append(aux)            
                aux = 0
                
        if flag == True:
            primero = min(resultados)
            segundo = max(resultados)
            print(f'{primero} {segundo}')
        

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
