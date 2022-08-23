key = int(input())
str_input = input()

for symbol in str_input:
    print(chr(97 + ((ord(symbol) % 97) - key) % 26), end=' ')
