#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
def diagonalDifference(arr):
    sum_diag_1 = 0
    sum_diag_2 = 0
    for i in range(n):
        sum_diag_1 += arr[i][i]
        sum_diag_2 += arr[i][n-1-i]
    return abs(sum_diag_1 - sum_diag_2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
