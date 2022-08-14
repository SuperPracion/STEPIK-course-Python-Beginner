from math import log

sum_nums = 1.0
start_num = int(input())

for i in range(1, start_num):
    sum_nums += (1 / (i + 1))

print(sum_nums - log(start_num))
