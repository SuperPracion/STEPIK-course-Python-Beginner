num_mass = [int(input()) for _ in range(3)]

print(max(num_mass))
print((num_mass[0] + num_mass[1] + num_mass [2]) - max(num_mass) - min(num_mass))
print(min(num_mass))