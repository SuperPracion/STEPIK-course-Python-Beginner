in_num = int(input())
min_num = 10
max_num = -1

while in_num:
    max_num = max(max_num, in_num % 10)
    min_num = min(min_num, in_num % 10)

    in_num //= 10

print('Максимальная цифра равна', max_num)
print('Минимальная цифра равна', min_num)
