# Consider a list (list = []). You can perform the following commands:
#
# insert i e: Insert integer e at position i.
# print: Print the list.
# remove e: Delete the first occurrence of integer .
# append e: Insert integer  at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.

# Initialize your list and read in the value of n  followed by  lines of commands where each command will be of the
# types listed above. Iterate through each command in order and perform the corresponding operation on your list.

#
# The first line contains an integer n, denoting the number of commands.
# Each line i of the n subsequent lines contains one of the commands described above.

if __name__ == '__main__':
    N = int(input())
    list_1 = []
    for n in range(N):
        x = input().split(" ")
        command = x[0]
        if command == "insert":
            list_1.insert(int(x[1]), int(x[2]))
        if command == "print":
            print(list_1)
        if command == "remove":
            list_1.remove(int(x[1]))
        if command == "append":
            list_1.append(int(x[1]))
        if command == "sort":
            list_1 = sorted(list_1)
        if command == "pop":
            list_1.pop()
        if command == "reverse":
            list_1 = list(reversed(list_1))

