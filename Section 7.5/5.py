in_num = int(input())
second_num = 0

while in_num > 9:
    second_num = in_num % 10
    in_num //= 10

print(second_num)
