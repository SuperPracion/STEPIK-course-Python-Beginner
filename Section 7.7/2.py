# this is a code review class
min_num = -10**6 - 1
sum_negative_nums = 0

for _ in range(10):
    x = int(input())
    if x < 0:
        sum_negative_nums += x
        if x > min_num:
            min_num = x

if sum_negative_nums < 0:
    print(sum_negative_nums, min_num, sep='\n')
else:
    print('NO')

