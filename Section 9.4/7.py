str_input = input()

if str_input.count('f') == 0:
    print('NO')
elif str_input.count('f') > 1:
    print(str_input.find('f'), str_input.rfind('f'))
else:
    print(str_input.find('f'))
