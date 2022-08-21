str_input = input()
sum_upper_sumbols = 0

for sumbol in str_input:
    if sumbol.islower():
        sum_upper_sumbols += 1

print(sum_upper_sumbols)