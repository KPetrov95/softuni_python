sequence_one = input().split(", ")
sequence_two = input().split(", ")
sequence_three = []
for word in sequence_one:
    for big_word in sequence_two:
        if word in big_word:
            sequence_three.append(word)
            break
print(sequence_three)