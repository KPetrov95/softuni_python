import re

phones = input()
phone_filter = '(\+359 2 \\d{3} \\d{4}\\b|\+359-2-\\d{3}-\\d{4})\\b'
result = re.findall(phone_filter, phones)

print(', '.join(result))