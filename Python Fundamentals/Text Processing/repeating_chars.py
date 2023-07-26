text = input()
final_text = ''
last_char = ''

for current_char in text:
    if current_char != last_char:
        final_text += current_char
    last_char = current_char

print(final_text)