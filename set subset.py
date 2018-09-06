# You are given two sets, A and B.
# Your job is to find whether set A is a subset of set B.
#
# If set A is subset of set B, print True.
# If set A is not a subset of set B, print False.
#
# Input Format
#
# The first line will contain the number of test cases, T.
# The first line of each test case contains the number of elements in set A.
# The second line of each test case contains the space separated elements of set A.
# The third line of each test case contains the number of elements in set B.
# The fourth line of each test case contains the space separated elements of set B.

T = int(input())
for x in range(T):
    A = int(input())
    A_set = set(input().split())
    B = int(input())
    B_set = set(input().split())
    print(A_set.issubset(B_set))
