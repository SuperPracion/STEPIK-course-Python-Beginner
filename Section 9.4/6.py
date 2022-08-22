str_input = input()
max_count_symbol = ''
sum_count_symbol = 0

for symbol in str_input:

    if str_input.count(symbol) >= sum_count_symbol:
        max_count_symbol = symbol
        sum_count_symbol = str_input.count(symbol)

print(max_count_symbol)