mass1 = input().split()
mass2 = input().split()

print(*[int(mass1[num]) + int(mass2[num]) for num in range(0, len(mass1))])