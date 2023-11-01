def valid_length(word):
    if len(word) in range(3, 16 + 1):
        return True
    return False


def valid_characters(word):
    for character in word:
        if not (character.isalnum() or character == '-' or character == '_'):
            return False
    return True


def redundant_characters(word):
    if ' ' in word:
        return False
    return True


def all_valid(word):
    if redundant_characters(word) and valid_characters(word) and valid_length(word):
        return True
    return False


words = input().split(", ")

for current_word in words:
    if all_valid(current_word):
        print(current_word)
