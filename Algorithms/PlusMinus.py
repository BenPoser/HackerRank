#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the plusMinus function below.
def plusMinus(arr):
    positive = 0
    negative = 0
    zeroes = 0
    length = len(arr)

    for i in arr:
        if i > 0:
            positive += 1
        elif i < 0:
            negative += 1
        else:
            zeroes += 1
    print(positive / length)
    print(negative / length)
    print(zeroes / length)


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
