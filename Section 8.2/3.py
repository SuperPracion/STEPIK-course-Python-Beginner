count = 0
maximum = -10**6 - 1
for _ in range(4):
    x = int(input())
    if x % 2 != 0:
        count += 1
        if x < 0 and x > maximum:
            maximum = x
        elif x > maximum:
            maximum = x

if count:
    print(count)
    print(maximum)
else:
    print('NO')