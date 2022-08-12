input_str = [len(input()) for _ in range(3)]

if sum(input_str) == (max(input_str) + min(input_str))/ 2 * 3:
    print('YES')
else:
    print('NO')