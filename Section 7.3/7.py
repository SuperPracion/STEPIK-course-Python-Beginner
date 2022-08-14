sum_divisors = 0
in_num = int(input())

for num in range(1,  in_num * 3):
    if in_num % num == 0:
        sum_divisors += num

print(sum_divisors)