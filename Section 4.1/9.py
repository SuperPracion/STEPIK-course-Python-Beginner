a, b, c = [int(input()) for _ in range(3)]
sum = 0

if a >= 0:
    sum += a
elif b >= 0:
    sum += b
elif c >= 0:
    sum += c

print(sum)