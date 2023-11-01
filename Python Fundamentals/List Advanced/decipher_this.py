message = input().split()

words = []

for word in message:
    int_str, char = "", ""

    for symbol in word:
        if symbol.isdigit():
            int_str += symbol
        else:
            char += symbol
    if len(char) == 1:
        modified_word = chr(int(int_str))+char
    else:
        modified_word = chr(int(int_str))+char[-1]+char[1:-1]+char[0]
    words.append(modified_word)

print(' '.join(words))