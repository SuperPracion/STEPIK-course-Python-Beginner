m, n = [int(input()) for _ in range(2)]

if m > n:
    for i in range(m, n - 1, -1):
        print(i)
elif n > m:
    for i in range(m, n + 1):
        print(i)
else:
    print(m)