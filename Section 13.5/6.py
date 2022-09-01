def is_palindrome(text):
    text = text.lower()
    for word in text:
        if word in (' ', ',', '.', '!', '?', '-'):
            text = text.replace(word, '')

    return True if text == text[::-1] else False

txt = input()

print(is_palindrome(txt))