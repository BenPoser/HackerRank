# You are given a set A and n other sets.
# Your job is to find whether set A is a strict superset of each of the N sets.
#
# Print True, if A is a strict superset of each of the N sets. Otherwise, print False.
#
# A strict superset has at least one element that does not exist in its subset.
#
# Input Format
#
# The first line contains the space separated elements of set A.
# The second line contains integer n, the number of other sets.
# The next n lines contains the space separated elements of the other sets.
#

# Output Format
#
# Print True if set A is a strict superset of all other N sets. Otherwise, print False.

set_list = []
set_A = set(input().split())
n = int(input())
for x in range(n):
    set_test = set(input().split())
    set_list.append(set_test)

for i in set_list:
    if not set_A.issuperset(i):
        result = False

print(result)



