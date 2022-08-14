a, b = [int(input()) for _ in range(2)]
sum_numbers_range = 0

for i in range(a , b + 1):
    cube_num = i**3
    if (cube_num % 10) == 4 or (cube_num % 10) == 9:
        sum_numbers_range += 1

print(sum_numbers_range)