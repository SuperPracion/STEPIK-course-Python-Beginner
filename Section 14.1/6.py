# объявление функции
def is_magic(date):
    flag_magic_date = False
    mass_date = [int(num) for num in date.split('.')]
    return mass_date[0] * mass_date[1] == mass_date[2] % 100

# считываем данные
date = input()

# вызываем функцию
print(is_magic(date))