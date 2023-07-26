repeated_string = lambda string, counts: string * counts


string_to_repeat = input()
counter = int(input())
print(repeated_string(string_to_repeat, counter))