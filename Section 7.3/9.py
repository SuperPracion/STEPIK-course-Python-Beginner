first_max = 0
second_max = 0

for _ in range(int(input())):
    in_num = int(input())

    if in_num > first_max:
        second_max = first_max
        first_max = in_num
    elif in_num > second_max:
        second_max = in_num
     
print(first_max, second_max, sep='\n')

