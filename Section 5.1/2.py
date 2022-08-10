x1, y1, x2, y2 = [int(input()) for _ in range(4)]

if (x1 + x2 + y1 + y2) % 4 == 0:
    print('YES')
else:
    print('NO')