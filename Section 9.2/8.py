in_str = input()
mid = len(in_str) % 2

print(in_str[len(in_str) // 2 + mid:] + in_str[:len(in_str) // 2 + mid])