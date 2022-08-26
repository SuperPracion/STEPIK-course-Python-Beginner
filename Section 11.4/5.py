language = [input() for _ in range(int(input()))]
search_word = input().lower()

for word in language:
    if search_word in word.lower():
        print(word)