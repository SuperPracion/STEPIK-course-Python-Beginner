start_x, start_y, fin_x, fin_y = [int(input()) for _ in range(4)]

if start_x == fin_x or start_y == fin_y:
    print('YES')
else:
    print('NO')