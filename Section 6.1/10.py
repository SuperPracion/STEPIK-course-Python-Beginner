num_mass = [int(i) for i in input()].sort()


if (num_mass[2] - num_mass[0] == num_mass[1]):
    print('Число интересное')
else:
    print('Число неинтересное')