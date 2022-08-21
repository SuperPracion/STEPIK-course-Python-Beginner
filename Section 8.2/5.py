in_num = int(input())

while in_num > 1000:
    in_num //= 10

print(in_num % 10)