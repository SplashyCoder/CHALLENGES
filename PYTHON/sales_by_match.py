#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    
    def quicksort(arr):
        if len(arr) <= 1:
            return arr
        else:
            pivot = arr[0]
            less_than_pivot = [x for x in arr[1:] if x <= pivot]
            greater_than_pivot = [x for x in arr[1:] if x > pivot]
            return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)
    
    def alone_deleted(ar,n):
        new_arr = []
        for i in range(0,n-1):
            #print(ar[i],ar[i+1])
            
            if ar[i] != ar[i+1] and ar[i] != ar[i-1] :
                #print('no pasa')
                pass
            
            if i == n-2 and ar[i] == ar[i+1]:
                #print('iguales')
                new_arr.append(ar[i])
                pass
            if (ar[i] == ar[i+1]) or (ar[i] != ar[i+1] and ar[i] == ar[i-1]):
                #print('pasa')
                new_arr.append(ar[i])
        return new_arr
        
    sorted_ar = quicksort(ar)
    new_sorted_ar = alone_deleted(sorted_ar,n)
    print(new_sorted_ar)
    
    result = 0
    result_acumulado = 0
    
    new_n = len(new_sorted_ar)
    '''
    for i in range(0,len(new_sorted_ar)-1,2):
        
        if new_sorted_ar[i] == new_sorted_ar[i+1]:
            print(new_sorted_ar[i],new_sorted_ar[i+1])
            result +=1
            
        result_acumulado +=1
            
        if new_sorted_ar[i] != new_sorted_ar[i+1]:
        '''
    for i in range(0, new_n-1):
        
        if i == new_n-2:
            print(new_sorted_ar[i],new_sorted_ar[i+1])  
            result_acumulado +=2
            print(result_acumulado)
            
            if result_acumulado%2!=0:
                result_acumulado +=1
                print('imparu')
                result += int((result_acumulado-1)/2)
                break
            
            if result_acumulado%2!=0 and result_acumulado == 2 :
                print('impari')
                result += 1
                break
            
            if result_acumulado%2==0:
                result_acumulado +=1
                print('paur')
                result += int(result_acumulado/2)
                break
            
            print(result_acumulado)
            print(result)
            break
        
        if (i == new_n-2 and new_sorted_ar[i] == new_sorted_ar[i+1]) or new_sorted_ar[i] != new_sorted_ar[i+1]  :
            print(new_sorted_ar[i],new_sorted_ar[i+1])  
            result_acumulado +=1
            print(result_acumulado)
            if result_acumulado%2!=0:
                print('impar')
                result += int((result_acumulado-1)/2)
            
            if result_acumulado%2==0:
                print('par')
                result += int(result_acumulado/2)
            
            result_acumulado = 0
            print(result_acumulado)
            print(result)
    
        if new_sorted_ar[i] == new_sorted_ar[i+1]:
            print(new_sorted_ar[i],new_sorted_ar[i+1])  
            result_acumulado +=1
            print(result_acumulado)
            
        
    print(new_sorted_ar)
    
    return result
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
