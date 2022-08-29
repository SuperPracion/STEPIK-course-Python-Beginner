words_mass = input().split()

for i in range(0, len(words_mass)):
    word = list(words_mass[i])
    firs_word = word[0]
    del word[0]
    word.append(firs_word)
    word.append('ки')
    words_mass[i] = ''.join(word)

print(*words_mass)



