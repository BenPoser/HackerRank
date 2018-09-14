phone_book = {}

n = int(input())
for _ in range(n):
    x = input().split()
    entry = {x[0]: x[1]}
    phone_book.update(entry)


for _ in range(n):
    name_check = input()
    check = phone_book.get(name_check, "Not found")
    if check == "Not found":
        print(check)
    else:
        print(name_check + "=" + phone_book[name_check])




