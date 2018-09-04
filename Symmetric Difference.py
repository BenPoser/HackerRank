# Task
# Given 2 sets of integers, M  and N , print their symmetric difference in ascending order. The term symmetric
# difference indicates those values that exist in either M or N  but do not exist in both.
#
# Input Format
#
# The first line of input contains an integer, M.
# The second line contains M space-separated integers.
# The third line contains an integer, N.
# The fourth line contains N space-separated integers.
#
# Output Format
#
# Output the symmetric difference integers in ascending order, one per line.

M = int(input())
MSet = set(input().split())
N = int(input())
NSet = set(input().split())

difference_set = MSet.difference(NSet)
difference_set.update(NSet.difference(MSet))
sorted_set = sorted(difference_set, key=int)
print("\n".join(sorted_set))

