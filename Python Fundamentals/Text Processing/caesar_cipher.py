text = input()
encrypted_text = ''

for i in range(len(text)):
    encrypted_text += chr(ord(text[i]) + 3)

print(encrypted_text)