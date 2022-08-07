a, b, c = [int(input()) for _ in range(3)]

if a < b < c > a:
    print(b)
elif a > b > c > a:
    print(a)
else:
    print(c)
