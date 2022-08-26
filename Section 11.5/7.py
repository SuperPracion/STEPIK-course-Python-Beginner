mass_num = input().split()
count_matches = 0

for i in range(len(mass_num)):
    for j in range(i + 1, len(mass_num)):
        if mass_num[i] == mass_num[j]:
            count_matches += 1

print(count_matches)