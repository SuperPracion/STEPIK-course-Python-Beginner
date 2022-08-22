str_input = input()

print(str_input.replace(
    str_input[str_input.find('h'):str_input.rfind('h') + 1],
    ''))