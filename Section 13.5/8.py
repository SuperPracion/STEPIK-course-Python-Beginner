def is_correct_bracket(text):
    for _ in range(len(text)):
        text = ''.join(text.split('()'))

    return text == ''

txt = input()

print(is_correct_bracket(txt))