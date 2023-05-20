word = input()
capital_letter = []
num_to_list = 0
for ch in word:
    if ch.isupper():
        capital_letter.append(num_to_list)
    num_to_list += 1

print(capital_letter)