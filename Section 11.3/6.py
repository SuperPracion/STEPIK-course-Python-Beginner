sum_mass = []
len_mass = int(input())
left_num = int(input())

for _ in range(len_mass - 1):
    int_input = int(input())
    sum_mass.append(int_input + left_num)
    left_num = int_input

print(sum_mass)