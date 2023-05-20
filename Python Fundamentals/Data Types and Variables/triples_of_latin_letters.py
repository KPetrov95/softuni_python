number_in_alphabet = int(input())

for character in range(number_in_alphabet):
    for character2 in range(number_in_alphabet):
        for character3 in range(number_in_alphabet):
            print(f'{chr(97 + character)}{chr(character2 + 97)}{chr(character3 + 97)}')
           