def get_factors(num):
    sum_divisors = 0
    for divisor in range(1, num + 1):
        if num % divisor == 0:
            sum_divisors += 1

    return sum_divisors

n = int(input())

print(get_factors(n))