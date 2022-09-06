decimal_answer = int(input())
hex_letter = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
hex_answer = ''

while decimal_answer:
    hex_num = decimal_answer % 16
    if hex_num in hex_letter:
        hex_answer += hex_letter[hex_num]
    else:
        hex_answer += str(hex_num)

    decimal_answer //= 16

print(hex_answer[::-1])