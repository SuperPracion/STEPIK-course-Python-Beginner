def get_days(month):
    days = 0
    if month == 2:
        days = 28
    elif month in (1, 3, 5, 7, 8, 10, 12):
        days = 31
    else:
        days = 30

    return days

num = int(input())

print(get_days(num))