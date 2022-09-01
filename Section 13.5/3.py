def get_next_prime(num):
    num += 1
    for i in range(num, num**2):
        count_divisors = 0
        for j in range(1, i + 1):
            if i % j == 0:
                count_divisors += 1
        if count_divisors == 2:
            return i

n = int(input())

print(get_next_prime(n))