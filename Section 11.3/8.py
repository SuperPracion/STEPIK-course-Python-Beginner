mass = [input() for _ in range(int(input()))]
out_symbol = int(input())

for el in mass:
    if len(el) >= out_symbol:
        print(el[out_symbol - 1], end='')
