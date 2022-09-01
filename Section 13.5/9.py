def convert_to_python_case(text):
    camel_cased = ''

    for i in range(len(text)):
        if text[i].isupper() and camel_cased != '':
                camel_cased += '_'
                camel_cased += text[i]
        else:
            camel_cased += text[i]

    return camel_cased.lower()

txt = input()

print(convert_to_python_case(txt))