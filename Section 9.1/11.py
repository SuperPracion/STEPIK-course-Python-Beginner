str_input = input()
sum_vowels = 0
sum_consonant = 0

for sumbol in str_input.lower():
    if sumbol in ('ауоыиэяюёе'):
        sum_vowels += 1
    if sumbol in ('бвгджзйклмнпрстфхцчшщ'):
        sum_consonant += 1

print(f'Количество гласных букв равно {sum_vowels}')
print(f'Количество согласных букв равно {sum_consonant}')