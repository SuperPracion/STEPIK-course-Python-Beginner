a, b = int(input()), int(input())

for num in range(a, b + 1):
    flag_dont_have_divisors = True
    for divider in range(2, num + 1):
        if num % divider == 0 and num != divider:
            flag_dont_have_divisors = False
            break

    if flag_dont_have_divisors and num != 1:
        print(num)