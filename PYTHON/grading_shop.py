#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    gradesFinal = []
    def check(number):
        if number < 38:
            gradesFinal.append(number)
        elif (number+1)%5 == 0:
            gradesFinal.append(number +1)
        elif (number+2)%5 == 0:
            gradesFinal.append(number + 2)
        else:
            gradesFinal.append(number)
    for i in grades:
        check(i)
        

    return(gradesFinal)

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
