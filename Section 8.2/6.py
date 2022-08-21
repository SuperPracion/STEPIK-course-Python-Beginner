in_num = int(input())

nums_of_triples = 0
nums_even = 0
sum_numbers_more_five = 0
product_numbers_move_seven = 1
nums_five_zero_in_num = 0
nums_of_last_num = 0
desired_las_num = in_num % 10

while in_num:
    last_num = in_num % 10

    if last_num == 3:
        nums_of_triples += 1

    if last_num == desired_las_num:
        nums_of_last_num += 1

    if last_num % 2 == 0:
        nums_even += 1

    if last_num > 5:
        sum_numbers_more_five += last_num

    if last_num > 7:
        product_numbers_move_seven *= last_num

    if last_num in (0, 5):
        nums_five_zero_in_num += 1

    in_num //= 10

print(nums_of_triples,
      nums_of_last_num,
      nums_even,
      sum_numbers_more_five,
      product_numbers_move_seven,
      nums_five_zero_in_num, sep='\n')