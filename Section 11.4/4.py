mass = []

for _ in range(int(input())):
    in_value = input()
    if in_value not in mass:
        mass.append(in_value)

print(*mass, sep='\n')