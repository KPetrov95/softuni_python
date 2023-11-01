word = input()
chars = ''
nums = ''
others = ''

for char in word:
    if char.isalpha():
        chars += char
    elif char.isdigit():
        nums += char
    else:
        others += char

print(nums)
print(chars)
print(others)
