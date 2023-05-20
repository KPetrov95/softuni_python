text = input().lower()

beach_list = ['sand', 'water', 'fish', 'sun']

sum_items = sum([text.count(word) for word in beach_list])

print(sum_items)
