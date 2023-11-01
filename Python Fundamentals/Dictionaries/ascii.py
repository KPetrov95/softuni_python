symbols = input().split(', ')
dictionary = {}

for symbol in symbols:
    if symbol not in dictionary.keys():
        dictionary[symbol] = ord(symbol)

print(dictionary)