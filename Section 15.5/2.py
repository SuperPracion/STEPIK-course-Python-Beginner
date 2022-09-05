def encryption_shift(init_line, num_shift):
    final_line = ' '
    for word in init_line:
        if word in ('abcdefghijklmnopqrstuvwxyz'):
            final_line += chr(97 + ((ord(word) % 97) - num_shift) % 26)
        elif word in ('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
            final_line += chr(65 + ((ord(word) % 65) - num_shift) % 26)
        else:
            final_line += word

    return final_line

for num in range(0, 26):
    print(encryption_shift('Hawnj pk swhg xabkna ukq nqj.', num))
