countries = input().split(', ')
capitals = input().split(', ')

matching_dictionary = {countries[index]: capitals[index] for index in range(len(countries))}

for country, capital in matching_dictionary.items():
    print(f'{country} -> {capital}')