text = input()

dict_symbols = {}

for symbol in text:
    if symbol not in dict_symbols:
        dict_symbols[symbol] = text.count(symbol)
for key, value in sorted(dict_symbols.items()):
    print(f'{key}: {value} time/s')
