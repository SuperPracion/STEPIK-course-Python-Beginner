mass_input = [int(input()) for _ in range(int(input()))]

print(*mass_input, sep='\n')

for num in mass_input:
    print(num ** 2 + 2 * num + num)