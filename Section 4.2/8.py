from math import sqrt

str_x, str_y, fin_x, fin_y = [int(input()) for _ in range(4)]

if (sqrt(str_x - fin_x) <= 1 or sqrt(str_y - fin_y) <= 1):
    print('YES')
else:
    print('NO')