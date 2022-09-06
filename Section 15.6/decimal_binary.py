decimal_list = int(input())
binary_list = ''

while decimal_list:
    binary_list += str(decimal_list % 2)

    decimal_list //= 2

print(binary_list[::-1])