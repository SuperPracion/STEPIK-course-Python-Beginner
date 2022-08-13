m, n = [int(input()) for _ in range(2)]

for i in range(n, m):
    if ((i % 17 == 0) or 
        (i % 10 == 9) or 
        (i % 3 == 0 and i % 5 == 0)):
        print(i)