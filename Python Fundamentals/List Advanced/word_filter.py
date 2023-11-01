all_words = input().split()

even_words =[word for word in all_words if len(word) % 2 == 0]

print('\n'.join(even_words))