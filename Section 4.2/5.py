a, b, c = [int(input()) for _ in range(3)]

if (a + b > c) or (a + c > b) or (b + c > a):
    print('YES')
else:
    print('NO')