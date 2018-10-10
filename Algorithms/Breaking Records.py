#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    high_score = scores[0]
    low_score = scores[0]
    break_high = 0
    break_low = 0
    for score in scores[1:]:
        if score > high_score:
            high_score = score
            break_high += 1
        elif score < low_score:
            low_score = score
            break_low += 1
    return break_high, break_low


if __name__ == '__main__':

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    print(result)