def check_type(some_type, some_input):
    if some_type == "int":
        some_input = int(some_input) * 2
        return some_input
    if some_type == "real":
        some_input = int(some_input) * 1.5
        return f'{some_input:.2f}'
    if some_type == 'string':
        return f'${some_input}$'


type_of_input = input()
word = input()
print(check_type(type_of_input,word))