in_num = int(input())

for divisor in range(2, in_num + 1):
    if in_num % divisor == 0:
        print(divisor)
        break
