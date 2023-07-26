words = input().split()
letters = {}

for word in words:
    if word.lower() not in letters:
        letters[word.lower()] = 0
    letters[word.lower()] += 1

for key, value in letters.items():
    if value % 2 != 0:
        print(key, end=' ')