sum_signals = 0

for _ in range(int(input())):
    if input().count('11') >= 3:
        sum_signals += 1

print(sum_signals)
