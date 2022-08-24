str_input = input()
count_f = str_input.count('f')

if 'f' not in str_input:
    print(count_f - 2)
else:
    print(str_input.replace('f', ' ', 1).find('f'))