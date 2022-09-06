hex_letter = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
hex_list = [num for num in input()[::-1]]
sum_hex_nums = 0

for num in range(len(hex_list)):
    if hex_list[num] in hex_letter:
        hex_list[num] = hex_letter[hex_list[num]]

for num in range(len(hex_list)):
    sum_hex_nums += int(hex_list[num]) * (16 ** num)

print(sum_hex_nums)
