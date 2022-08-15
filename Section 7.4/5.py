in_num = int(input())
sum_positive_nums = 0

while in_num > -1:
    sum_positive_nums += in_num
    in_num = int(input())
    
print(sum_positive_nums)