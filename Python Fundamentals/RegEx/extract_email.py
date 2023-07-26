import re

text = input()
#pattern = r'\b(([a-z0-9]+[a-z\.\-\_]*)@([A-Za-z]+[-\.a-z]*))\b'
pattern = r'\s(([a-z0-9]+[a-z0-9\.\-\_]*)@([a-z\-]+)(\.[a-z]+)+)\b'

result = re.findall(pattern, text)

for current_email in result:
    print(current_email[0])