sentence_mass = [input() for _ in range(int(input()))]
word_search = [input().lower() for _ in range(int(input()))]

out_mass = []

for sentence in sentence_mass:
    flag_in = 0
    for word in word_search:
        if word in sentence.lower():
            flag_in += 1

    if flag_in >= len(word_search):
        out_mass.append(sentence)

print(*out_mass, sep='\n')