month = int(input())

if month in [2]:
    print(28)
elif month in [4, 6, 9, 11]:
    print(30)
else:
    print(31)