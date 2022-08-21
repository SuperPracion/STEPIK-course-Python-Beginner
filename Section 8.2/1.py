n = int(input())
s = 0
while n:
    if n % 2 == 0:
        s += n % 10
    n //= 10
print(s)