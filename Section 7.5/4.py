in_num = int(input())

sum_nums = 0
number_of_nums = 0
product_of_nums = 1
first_num = 0
sum_of_first_last = in_num % 10

while in_num:
    last_num = in_num % 10

    sum_nums += last_num
    number_of_nums += 1
    product_of_nums *= last_num
    first_num = last_num

    in_num //= 10

print(sum_nums, number_of_nums,
      product_of_nums,
      sum_nums / number_of_nums,
      first_num,
      sum_of_first_last + first_num, sep='\n')
