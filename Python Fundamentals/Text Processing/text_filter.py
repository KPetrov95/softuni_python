banned_words = input().split(", ")
text = input()

for i in range(len(banned_words)):
    if banned_words[i] in text:
        text = text.replace(banned_words[i], "*" * len(banned_words[i]))

print(text)