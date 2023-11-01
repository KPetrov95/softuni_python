import re

names = input()
filter = '\\b[A-Z][a-z]+ [A-Z][a-z]+\\b'
result = re.findall(filter, names)
print(' '.join(result))