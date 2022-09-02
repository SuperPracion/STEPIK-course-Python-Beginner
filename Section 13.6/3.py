from math import *

def solve(a, b, c):
    D  = pow(b, 2) - 4 * a * c
    x1 = x2 = 0

    if D > 0:
        x1 = (-b - sqrt(D)) / (2 * a)
        x2 = (-b + sqrt(D)) / (2 * a)
    else:
        x1 = x2 = (-b / (a * 2))

    return min(x1, x2), max(x1, x2)

a, b, c = int(input()), int(input()), int(input())

x1, x2 = solve(a, b, c)
print(x1, x2)