in_num = int(input())

for num in range(1, in_num + 1):
    if 5 <= num <= 9:
        continue
    if 17 <= num <= 37:
        continue
    if 78 <= num <= 87:
        continue
    print(num)
