# You like all the integers in set A and dislike all the integers in set B. Your initial happiness is 0.
#  For each i integer in the array you like add 1 to your happiness. If you don't like add -1 to your happiness.

# Input Format
#
# The first line contains integers n and m separated by a space.
# The second line contains n integers, the elements of the array.
# The third and fourth lines contain m integers, A and B, respectively.
#
# Output Format
#
# Output a single integer, your total happiness.

x = input()
array_set = set(input().split())
A = set(input().split())
B = set(input().split())

happiness = 0

for i in array_set:
    if i in A:
        happiness += 1

for i in array_set:
    if i in B:
        happiness -= 1

print(happiness)



