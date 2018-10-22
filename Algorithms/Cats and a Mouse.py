#!/bin/python3

import math
import os
import random
import re
import sys
#x = Cat A
# y = Cat B
# z = Mouse C
# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    Cat_A_distance = abs(x-z)
    Cat_B_distance = abs(y-z)
    if Cat_A_distance > Cat_B_distance:
        return "Cat B"
    if Cat_B_distance > Cat_A_distance:
        return "Cat A"
    if Cat_B_distance == Cat_A_distance:
        return "Mouse C"



if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        print(result)
