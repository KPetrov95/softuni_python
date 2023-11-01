import re

text = input()
pattern = r'(w{3})\.([A-Za-z0-9\-.]+)\.([a-z\.]+)'

while text:
    result = re.search(pattern, text)
    if result:
        print(result.group())
    text = input()