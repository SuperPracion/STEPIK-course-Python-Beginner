num = int(input())

if 1000 <= num <= 9999 and (num % 7 == 0 or num % 17 == 0):
    print('YES')
else:
    print('NO')