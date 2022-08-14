product_nums = 1

for _ in range(10):
    input_num = int(input())
    if input_num != 0:
        product_nums *= input_num

print(product_nums)