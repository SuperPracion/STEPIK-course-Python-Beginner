def find_all(target, symbol):
    mass_search = []
    for word in range(len(target)):
        if target[word] == symbol:
            mass_search.append(target.index(symbol, word))

    return mass_search

s = input()
char = input()

print(find_all(s, char))