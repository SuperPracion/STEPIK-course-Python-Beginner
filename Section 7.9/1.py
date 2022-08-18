in_num = int(input())
search_nums = 1

for i in range(in_num):
    for _ in range(i + 1):
        print(search_nums, end=' ')
        search_nums += 1
    print()
