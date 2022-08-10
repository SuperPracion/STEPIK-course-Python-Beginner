x1, y1, x2, y2 = [int(input()) for _ in range(4)]

if abs(x1 - x2) - abs(y1 - y2) == 0:
    print('YES')
else:
    print('NO')