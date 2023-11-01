text = input()

chars = {}

for char in text:
    if char != ' ':
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1

for char, occurences in chars.items():
    print(f'{char} -> {occurences}')
