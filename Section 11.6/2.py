mass = [int(x) for x in input().split()]

max_num = mass.index(max(mass))
min_num = mass.index(min(mass))

mass[max_num], mass[min_num] = mass[min_num], mass[max_num]

print(*mass, sep=' ')