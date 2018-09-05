# TASK
# You are given a set  and  number of other sets. These  number of sets have to perform some specific mutation
# operations on set .
#
# Your task is to execute those operations and print the sum of elements from set .
#
# Input Format
#
# The first line contains the number of elements in set A.
# The second line contains the space separated list of elements in set A.
# The third line contains integer N, the number of other sets.
# The next 2*N lines are divided into N parts containing two lines each.
# The first line of each part contains the space separated entries of the operation name and the length of the other set
# The second line of each part contains space separated list of elements in the other set.
#
# Output Format
#
# Output the sum of elements in set A.

nA = int(input())
A = set(map(int, input().split()))
N = int(input())

for nA in range(N):
    (command, newSet) = (
        input().split()[0],
        set(map(int, input().split()))
    )

    getattr(A, command)(newSet)

print(sum(A))
