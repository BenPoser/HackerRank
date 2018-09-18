#!/bin/python3

import math
import os
import random
import re
import sys
# Task
# Given a base-10 integer,n , convert it to binary (base-2). Then find and print the base-10 integer
# denoting the maximum number of consecutive 1's in n's binary representation.


if __name__ == '__main__':
    n = int(input())

    bi = str(bin(n)[2:]).split("0")
    length = [len(one) for one in bi]
    print(max(length))


