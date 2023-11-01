words = input().split()
new_list = []
while True:
    message = input().split()
    if message[0] == '3:1':
        break
    if message[0] == 'merge':
        start_index = int(message[1])
        end_index = int(message[2])
        element_to_merge = ''
        for word in words[start_index:end_index + 1]:
            element_to_merge += word
            words[start_index] = element_to_merge
            words.remove(word)
print(words)