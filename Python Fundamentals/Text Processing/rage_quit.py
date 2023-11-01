text = input().upper()
current_symbols = ''
multiplier = ''
final_symbols = ''

for index in range(len(text)):
    if not text[index].isdigit():
        current_symbols += text[index]
    else:
        for next_index in range(index, len(text)):
            if not text[next_index].isdigit():
                break
            multiplier += text[next_index]
        final_symbols += current_symbols * int(multiplier)
        current_symbols = ''
        multiplier = ''

print(f'Unique symbols used: {len(set(final_symbols))}')
print(final_symbols)