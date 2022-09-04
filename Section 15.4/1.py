from random import *

dict_password_characters = {'digits': '0123456789',
                            'lowercase_letters': 'abcdefghijklmnopqrstuvwxyz',
                            'uppercase_letters': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
                            'punctuation': '!#$%&*+-=?@^_'}

positive_response_list = ['да', 'ага', 'конечно', 'дэ', 'угу']


def generate_password(list_flags, len_pass):
    character_array = ''
    for flag in list_flags:
        if flag:
            character_array += dict_password_characters[flag]

    return ''.join(sample(str(character_array), len_pass))


def drawing_criteria():
    array_criteria = []

    print('Использовать цифры?')
    if input() in positive_response_list:
        array_criteria.append('digits')

    print('Нижний регистр букв?')
    if input() in positive_response_list:
        array_criteria.append('lowercase_letters')

    print('Верхний регистр букв?')
    if input() in positive_response_list:
        array_criteria.append('uppercase_letters')

    print('Специальные символы?')
    if input() in positive_response_list:
        array_criteria.append('punctuation')

    return array_criteria


mass_flags = drawing_criteria()
len_pass = int(input())
print(generate_password(mass_flags, len_pass))