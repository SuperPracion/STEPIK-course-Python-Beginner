year = [int(i) for i in str(input())]
mass_leng = len(year)

if year[mass_leng - 1] or year[mass_leng - 2]:
    print('NO')
else:
    print('YES')