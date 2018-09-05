# Task
# You have a non-empty set s, and you have to execute N commands given in N lines.
#
# The commands will be pop, remove and discard.

n = int(input())
s = set(map(int, input().split()))
p = int(input())

for i in range(p):
    x = input().split(" ")
    command = x[0]
    if command == "pop":
        s.pop()
    if command == "remove":
        s.remove(int(x[1]))
    if command == "discard":
        s.discard(int(x[1]))

print(sum(s))

