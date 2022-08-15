nums_fives = 0
in_num = int(input())

while -1 < in_num < 6:
    if in_num == 5:
        nums_fives += 1
    in_num = int(input())

print(nums_fives)