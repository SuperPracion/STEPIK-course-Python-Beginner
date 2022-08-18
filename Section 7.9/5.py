in_num = int(input())

while in_num >= 10:
    sum_nums = 0
    while in_num:
        sum_nums += in_num % 10
        in_num //= 10

    in_num = sum_nums

print(in_num)