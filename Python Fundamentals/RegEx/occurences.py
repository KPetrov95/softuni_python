import re

text = input()
target_word = input()
pattern = fr'(?i)\b{target_word}\b'
result = re.findall(pattern, text)

print(len(result))