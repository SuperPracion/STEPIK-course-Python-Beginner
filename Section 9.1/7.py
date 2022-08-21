in_str = input()

for sumbol in in_str:
    if sumbol in ('1234567890'):
        print('Цифра')
        break
else:
    print('Цифр нет')