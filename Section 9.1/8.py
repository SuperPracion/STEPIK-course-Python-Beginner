str_input = input()
sum_pluse = 0
sum_star = 0

for sumbol in str_input:
    if sumbol == '+':
        sum_pluse += 1
    if sumbol == '*':
        sum_star += 1

print(f'Символ + встречается {sum_pluse} раз')
print(f'Символ * встречается {sum_star} раз')