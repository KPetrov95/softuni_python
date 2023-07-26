import re

numbers = input()

pattern = r'((^|(?<=\s))-?([0-9]|[1-9][0-9]*\.?\d*)($|(?=\s)))'

result = re.findall(pattern, numbers)

for current_number in result:
    print(current_number[0], end=' ')