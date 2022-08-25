alphabet = []

for len in range(1, 27):
    alphabet.append(chr(96 + len) * len)

print(alphabet)