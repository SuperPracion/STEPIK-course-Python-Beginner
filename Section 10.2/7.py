str_input = input()

for symbol in range(len(str_input)):
    if symbol % 3 != 0:
        print(str_input[symbol], end='')