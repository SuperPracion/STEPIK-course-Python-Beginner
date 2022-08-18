in_num = int(input())

for num in range(1, in_num + 1):
    sum_divisors = 0
    for divider in range(1, num + 1):
        if num % divider == 0:
            sum_divisors += 1

    print(num, '+' * sum_divisors, sep='')