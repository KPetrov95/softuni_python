def reverse_text(string: str):
    start_index = len(string) - 1
    end_index = -1
    while start_index > end_index:
        yield string[start_index]
        start_index -= 1

for char in reverse_text("step"):
    print(char, end='')
