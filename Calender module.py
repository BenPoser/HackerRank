import calendar

d, m, y = map(int, input().split())
print((calendar.day_name[calendar.weekday(y, m, d)]).upper())
