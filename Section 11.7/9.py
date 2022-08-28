in_num = [int(num) ** 2 for num in input().split() if int(num) % 2 == 0 and int(num) ** 2 % 10 != 4]

print(*in_num, sep=' ')
