in_str = input()
adjacent_sumbols = 0

for sumbol in range(0, len(in_str) - 1):
    if in_str[sumbol] == in_str[sumbol + 1]:
        adjacent_sumbols += 1

print(adjacent_sumbols)