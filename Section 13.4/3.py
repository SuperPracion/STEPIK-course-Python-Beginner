def get_factors(num):
    divisors = []
    for divisor in range(1, num + 1):
        if num % divisor == 0:
            divisors.append(divisor)

    return divisors

n = int(input())

print(get_factors(n))