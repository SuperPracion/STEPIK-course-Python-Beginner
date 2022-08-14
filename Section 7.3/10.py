flag_even = True

for _ in range(10):
    if int(input()) % 2 != 0:
        flag_even = False

print('YES' if flag_even else 'NO')