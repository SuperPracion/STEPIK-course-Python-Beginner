#КТО СПИСЫВАЕТ - ТО ЧЁРТ
a, b = int(input()), int(input())

desired_num = 0
sum_desires_nums = 0
#КТО СПИСЫВАЕТ - ТО ЧЁРТ
for num in range(a, b + 1):
    favorite_num = 0
    sum_divisors = 0
    # КТО СПИСЫВАЕТ - ТО ЧЁРТ
    for divider in range(1, num + 1):
        if num % divider == 0:
            favorite_num = num
            sum_divisors += divider

    if sum_divisors >= sum_desires_nums:
        desired_num = favorite_num
        sum_desires_nums = sum_divisors
    # КТО СПИСЫВАЕТ - ТО ЧЁРТ
print(desired_num, sum_desires_nums, sep=' ')
#КТО СПИСЫВАЕТ - ТО ЧЁРТ