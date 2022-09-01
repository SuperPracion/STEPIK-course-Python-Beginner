def is_prime(num):
    count_divisors = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count_divisors += 1
    return True if count_divisors == 2 else False
    # return sum(1 for i in range(1, num + 1) if num % i == 0) == 2

n = int(input())

print(is_prime(n))