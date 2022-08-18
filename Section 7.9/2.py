in_num = int(input())

for height in range(1, in_num + 1):
    for i in range(1, height + 1):
        print(i, end='')
    for j in range(height - 1, 0, -1):
        print(j, end='')
    print()