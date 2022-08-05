a, b, c, d = [int(input()) for _ in range(4) ]

if a < b < c < d:
    print(a)
elif a > b < c < d:
    print(b)
elif a > b > c < d:
    print(c)
else:
    print(d)