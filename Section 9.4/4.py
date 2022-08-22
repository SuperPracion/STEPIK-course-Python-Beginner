str_input = input()
nums_num = 0

for num in range(0, 10):
    nums_num += str_input.count(str(num))

print(nums_num)