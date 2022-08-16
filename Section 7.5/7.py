in_num = int(input())

while in_num // 10 % 10 >= in_num % 10:
    in_num //= 10

print('YES' if in_num < 10 else 'NO')
