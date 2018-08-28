# You are given a 2-D array with dimensions N X M.
# Your task is to perform the min function over axis 1 and then find the max of that.
#
# Input Format
#
# The first line of input contains the space separated values of N and M.
# The next N lines contains M space separated integers.

import numpy

n, m = map(int, input().split())
a = numpy.array([input().split() for _ in range(n)], int)
find_min = numpy.min(a, axis=1)
find_max = numpy.max(find_min, axis=0)

print(find_max)