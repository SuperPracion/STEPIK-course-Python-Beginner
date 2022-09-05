#right = '-'
#left = '+'

def encryption_shift(init_line, num_shift, language):
    final_line = ' '

    match language:
        case 'ru':
            for word in init_line:
                if word in ('абвгдежзийклмнопрстуфхцчшщъыьэюя'):
                    final_line += chr(1072 + ((ord(word) % 1072) - num_shift) % 32)
                elif word in ('АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'):
                    final_line += chr(1040 + ((ord(word) % 1040) - num_shift) % 32)
                else:
                    final_line += word
        case 'en':
            for word in init_line:
                if word in ('abcdefghijklmnopqrstuvwxyz'):
                    final_line += chr(97 + ((ord(word) % 97) - num_shift) % 26)
                elif word in ('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
                    final_line += chr(65 + ((ord(word) % 65) - num_shift) % 26)
                else:
                    final_line += word
        case _:
            pass

    # print(ord('a'), ord('A'))

    return final_line.strip()

init_line = input().split(' ')
# num_shift = int(input())
# language = input()

for line in init_line:
    print(encryption_shift(line, -len([1 for word in line if word.isalpha()]), 'en'), end=' ')
