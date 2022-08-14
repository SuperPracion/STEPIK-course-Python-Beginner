sum_nums_sqrt = 0

for num in range(1, int(input()) + 1):
    end_num = num**2 % 10
    if end_num in (2, 5, 8):
        sum_nums_sqrt += num

print(sum_nums_sqrt)