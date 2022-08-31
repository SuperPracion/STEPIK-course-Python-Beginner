def mass_inp_sort(n):
    mass_input = []
    for _ in range(n):
        mass_input += [int(num) for num in input().split()]

    mass_input.sort()
    return mass_input

n = int(input())
print(*mass_inp_sort(n))