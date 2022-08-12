from math import *

a, b, c = [float(input()) for _ in range(3)]
D = b**2 - 4 * a * c

if D > 0:
    print(-b + sqrt(D) / 2*a)
    print(-b - sqrt(D) / 2*a)
elif D == 0:
    print(-(b / a*2))
else:
    print('NO')