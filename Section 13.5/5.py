def is_one_away(word1, word2):
    flag_only_thing = True

    if len(word1) == len(word2):
        if sum(1 for i in range(0, len(word1)) if word1[i] != word2[i]) > 1:
            flag_only_thing = False
    else:
        flag_only_thing = False

    return flag_only_thing

txt1 = input()
txt2 = input()

print(is_one_away(txt1, txt2))