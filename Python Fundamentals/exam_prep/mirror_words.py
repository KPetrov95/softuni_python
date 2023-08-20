import re

string_of_words = input()
pattern = r'([@#])([A-Za-z]{3,})\1\1([A-Za-z]{3,})\1'
result = re.findall(pattern, string_of_words)
mirror_words = []

for match in result:
    if match[1] == match[2][::-1]:
        mirror_words.append(f'{match[1]} <=> {match[2]}')

if not result:
    print("No word pairs found!")
else:
    print(f"{len(result)} word pairs found!")
if len(mirror_words) < 1:
    print("No mirror words!")
else:
    print('The mirror words are:')
    print(', '.join(mirror_words))